#include "codexion.h"

void    smart_sleep(t_hub*hub, long duration_ms)
{
    long    start_time = get_time_ms();

    while (hub->simulation_active)
    {
        if (get_time_ms() - start_time >= duration_ms)
            break;
        usleep(500);
    }
}

void    print_state(t_hub   *hub, int   id, char    *state)
{
    pthread_mutex_lock(&hub->write_lock);
    if (hub->simulation_active)
        printf ("%ld %d %s\n", get_time_ms() - hub->start_time, id, state);
    pthread_mutex_unlock(&hub->write_lock);
}

void    acq_single_d(t_coder    *coder, t_dongle    *dongle)
{
    long    priority_score;
    pthread_mutex_lock(&dongle->lock);


    if (coder->hub->scheduler == SCHED_FIFO)
        priority_score = get_time_ms();
    else
        priority_score = coder->last_compile_start + coder->hub->time_to_burnout;

    push_to_heap(&dongle->queue, coder->id, priority_score);
    while (coder->hub->simulation_active &&
          (dongle->is_held ||
            get_time_ms() < dongle->available_at ||
            dongle->queue.requests[0].coder_id != coder->id))
    {
        pthread_cond_wait(&dongle->cv, &dongle->lock);
    }

    if (!coder->hub->simulation_active)
    {
        pthread_mutex_unlock(&dongle->lock);
        return;
    }

    pop_from_heap(&dongle->queue);
    dongle->is_held = 1;
    pthread_mutex_unlock(&dongle->lock);
    print_state(coder->hub, coder->id, "has taken a dongle");
}

void    rel_single_d(t_coder    *coder, t_dongle    *dongle)
{
    pthread_mutex_lock(&dongle->lock);
    dongle->is_held = 0;
    dongle->available_at = get_time_ms() + coder->hub->dongle_cooldown;
    pthread_cond_broadcast(&dongle->cv);
    pthread_mutex_unlock(&dongle->lock);
}

void    *coder_routine(void *arg)
{
    t_coder *coder = (t_coder   *)arg;
    t_dongle    *first_dongle;
    t_dongle    *second_dongle;


    if (coder->id % 2 == 0)
    {
        first_dongle = coder->left_dongle;
        second_dongle = coder->right_dongle;
    }
    else
    {
        first_dongle = coder->right_dongle;
        second_dongle = coder->left_dongle;
    }

    while (coder->hub->simulation_active)
    {
        acq_single_d(coder, first_dongle);
        if (!coder->hub->simulation_active) break;
        acq_single_d(coder, second_dongle);
        if (!coder->hub->simulation_active) break;

        pthread_mutex_lock(&coder->hub->state_lock);
        coder->last_compile_start = get_time_ms();
        coder->compiles_done++;
        pthread_mutex_unlock(&coder->hub->state_lock);
        print_state(coder->hub, coder->id, "is compiling");
        smart_sleep(coder->hub, coder->hub->time_to_compile);

        rel_single_d(coder, second_dongle);
        rel_single_d(coder, first_dongle);


        if (coder->hub->required_compiles > 0 && coder->compiles_done >= coder->hub->required_compiles)
            break;
        print_state(coder->hub, coder->id, "is debugging");
        smart_sleep(coder->hub, coder->hub->time_to_debug);

        print_state(coder->hub, coder->id, "is refactoring");
        smart_sleep(coder->hub, coder->hub->time_to_refactor);
    }
    return (NULL);
}
