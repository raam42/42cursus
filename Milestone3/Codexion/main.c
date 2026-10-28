#include "codexion.h"

<<<<<<< HEAD
=======

>>>>>>> refs/remotes/origin/main
static void init_mutexes(t_hub  *hub)
{
    int i;

    i = 0;
    while (i < hub->num_coders)
    {
        pthread_mutex_init(&hub->dongles[i].lock, NULL);
        pthread_cond_init(&hub->dongles[i].cv, NULL);
        hub->dongles[i].is_held = 0;
        hub->dongles[i].available_at = 0;
        hub->dongles[i].queue.capacity = hub->num_coders;
        hub->dongles[i].queue.size = 0;
        hub->dongles[i].queue.requests = malloc(sizeof(t_request) \
                                            * hub->num_coders);
        i++;
    }
}

static void init_coders(t_hub   *hub)
{
    int i;
    int next;

    hub->start_time = get_time_ms();
    i = 0;
<<<<<<< HEAD
    while (i < hub->num_coders)
    {
        next = (i + 1) % hub->num_coders;
        hub->coders[i].id = i + 1;
        hub->coders[i].compiles_done = 0;
        hub->coders[i].last_compile_start = hub->start_time;
        hub->coders[i].hub = hub;
        hub->coders[i].left_dongle = &hub->dongles[i];
        hub->coders[i].right_dongle = &hub->dongles[next];
        i++;
    }
}

static void start_and_join(t_hub    *hub)
{
    pthread_t   monitor;
    int i;

    i = 0;
    while (i < hub->num_coders)
    {
        pthread_create(&hub->coders[i].thread, NULL, \
                                coder_routine, &hub->coders[i]);
        i++;
    }
    pthread_create(&monitor, NULL, monitor_routine, hub);
    pthread_join(monitor, NULL);
    i = 0;
    while (i < hub->num_coders)
    {
        pthread_join(hub->coders[i].thread, NULL);
        i++;
    }
}

static void cleanup_hub(t_hub   *hub)
{
    int i;

    i = 0;
    while (i < hub->num_coders)
    {
        pthread_mutex_destroy(&hub->dongles[i].lock);
        pthread_cond_destroy(&hub->dongles[i].cv);
        free(hub->dongles[i].queue.requests);
        i++;
    }
    pthread_mutex_destroy(&hub->write_lock);
    pthread_mutex_destroy(&hub->state_lock);
    free(hub->dongles);
    free(hub->coders);
}

=======
    while ()
}
>>>>>>> refs/remotes/origin/main
int main(int    argc, char  **argv)
{
    t_hub   hub;

    if (!val_args(argc, argv))
        return (1);
    if (!init_hub(&hub, argv))
        return (1);
    init_mutexes(&hub);
    init_coders(&hub);
    start_and_join(&hub);
    cleanup_hub(&hub);
    return (0);
}
