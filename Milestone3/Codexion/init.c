#include "codexion.h"


int is_num_str(const char   *str)
{
    int i = 0;

    
    if (!str || str[0] == '\0')
        return (0);
    if (str[0] == '-')
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

int val_args(int    argc, char  **argv)
{
    int i = 1;


    if (argc != 9)
    {
        printf ("Error: Codexion requires exactly 8 arguments.\n");
        return (0);
    }

    while (i <= 7)
    {
        if (!is_num_str(argv[i]))
        {
            printf ("Error: Argument %d ('%s) is not a valid positive integer.\n", i, argv[i]);
            return (0);
        }
        i++;
    }

    if (strcmp(argv[8], "fifo") != 0 && strcmp(argv[8], "edf") != 0)
    {
        printf ("Error: Scheduler must be exactly 'fifo' or 'edf'.\n");
        return (0);
    }
    return (1);
}

int init_hub(t_hub  *hub, int   argc, char  **argv)
{
    (void)argc;
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
        hub->scheduler = SCHED_FIFO;

    hub->dongles = malloc(sizeof(t_dongle) * hub->num_coders);
    hub->coders = malloc(sizeof(t_coder) * hub->num_coders);


    if (!hub->dongles || !hub->coders)
        return (0);
    return (1);
}
