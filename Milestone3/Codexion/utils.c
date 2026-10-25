#include "codexion.h"

void    wake_all_coders(t_hub   *hub)
{
    int i = 0;

    while (i < hub->num_coders)
    {
        pthread_mutex_lock(&hub->dongles[i].lock);
        pthread_cond_broadcast(&hub->dongles[i].cv);
        pthread_mutex_unlock(&hub->dongles[i].lock);
        i++;
    }
}

long    get_time_ms(void)
{
    struct  timeval tv;
    gettimeofday(&tv, NULL);
    return ((tv.tv_sec * 1000) + (tv.tv_usec / 1000));
}

void    *monitor_routine(void *arg)
{
    t_hub   *hub = (t_hub *)arg;
    int i;
    int finished_coders;
    long    current_time;

    while (1)
    {
        finished_coders = 0;
        i = 0;


        pthread_mutex_lock(&hub->state_lock);

        while (i < hub->num_coders)
        {
            current_time = get_time_ms();

            if (current_time - hub->coders[i].last_compile_start >= hub->time_to_burnout)
            {
                pthread_mutex_lock(&hub->write_lock);
                printf ("%ld %d burned out \n", current_time - hub ->start_time, hub->coders[i].id);
                hub->simulation_active = 0;
                pthread_mutex_unlock(&hub->write_lock);
                pthread_mutex_unlock(&hub->state_lock);

                wake_all_coders(hub);
                return (NULL);
            }

            if (hub->required_compiles > 0 && hub->coders[i].compiles_done >= hub->required_compiles)
                finished_coders++;
            i++;
        }

        if (hub->required_compiles > 0 && finished_coders == hub->num_coders)
        {
            hub->simulation_active = 0;
            pthread_mutex_unlock(&hub->state_lock);

            wake_all_coders(hub);
            return (NULL);
        }
        
        pthread_mutex_unlock(&hub->state_lock);
        usleep(1000);
    }
    return (NULL);
}