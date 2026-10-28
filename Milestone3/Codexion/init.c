#include "codexion.h"

long    get_time_ms(void)
{
    struct timeval  tv;

    gettimeofday(&tv, NULL);
    return ((tv.tv_sec * 1000) + (tv.tv_usec / 1000));
}

int is_num_str(const char   *str)
{
    int i;

    i = 0;
    if (!str || str[0] == '\0' || str[0] == '-')
        return (0);
    if (str[0] == '+')
        i++;
    if (str[i] == '\0')
        return (0);
    while (str[i])
    {
        if (str[i] < '0' || str[i] > '9')
            return (0);
        i++;
    }
    return (1);
}

static int  check_args(char **argv)
{
    if (atoi(argv[1]) <= 0)
    {
        printf ("Error: number of coders must be greater than 0.\n");
        return (0);
    }
    if (strcmp(argv[8], "fifo") != 0 && strcmp(argv[8], "edf") != 0)
    {
        printf ("Error: Scheduler must be exactly 'fifo' or 'edf'.\n");
        return (0);
    }
    return (1);
}

int val_args(int    argc, char  **argv)
{
    int i;

    i = 1;
    if (argc != 9)
    {
        printf ("Error: Codexion requires exactly 8 arguments.\n");
        return (0);
    }
    while (i <= 7)
    {
        if (!is_num_str(argv[i]))
        {
            printf ("Error: Argument %d(%s) is not a valid positive integer.\n", i, argv[i]);
            return (0);
        }
        i++;
    }

int init_hub(t_hub  *hub, char  **argv)
{
    hub->num_coders = atoi(argv[1]);
    hub->time_to_burnout = atoi(argv[2]);
    hub->time_to_compile = atoi(argv[3]);
    hub->time_to_debug = atoi(argv[4]);
    hub->time_to_refactor = atoi(argv[5]);
    hub->required_compiles = atoi(argv[6]);
    hub->dongle_cooldown = atoi(argv[7]);
    if (strcmp(argv[8], "edf") == 0)
        hub->scheduler = POLICY_EDF;
    else
        hub->scheduler = POLICY_FIFO;
<<<<<<< HEAD
=======

>>>>>>> refs/remotes/origin/main
    hub->simulation_active = 1;
    pthread_mutex_init(&hub->write_lock, NULL);
    pthread_mutex_init(&hub->state_lock, NULL);
    hub->dongles = malloc(sizeof(t_dongle) * hub->num_coders);
    hub->coders = malloc(sizeof(t_coder) * hub->num_coders);
    if (!hub->dongles || !hub->coders)
        return (0);
    return (1);
}