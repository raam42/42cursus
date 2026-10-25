#ifndef CODEXION_H
# define CODEXION_H

#include <pthread.h>
#include <sys/time.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

typedef struct s_hub    t_hub;


typedef enum e_scheduler
{
    SCHED_FIFO,
    SCHED_EDF
}   t_scheduler;


typedef struct s_request
{
    int coder_id;
    long    priority_score;
}   t_request;


typedef struct s_pqueue
{
    t_request   *requests;
    int size;
    int capacity;
}   t_pqueue;


typedef struct  s_dongle
{
    pthread_mutex_t lock;
    pthread_cond_t  cv;
    long    available_at;
    int is_held;
    t_pqueue    queue;
}   t_dongle;


typedef struct  s_coder
{
    int id;
    pthread_t   thread;
    long    last_comp_start;
    int comp_done;
    t_dongle    *left;
    t_dongle    *right;
    t_hub   *hub;
}   t_coder;


struct  s_hub
{
    int num_coders;
    long    time_to_burn;
    long    time_to_comp;
    long    time_to_deb;
    long    time_ti_ref;
    int req_comp;
    long    d_cooldown;
    t_scheduler scheduler;

    long    strt_time;
    int sim_active;

    pthread_mutex_t write_lock;
    pthread_mutex_t state_lock;

    t_dongle    *dongles;
    t_coder *coders;
};


void    swap_requests(t_requests    *a, t_request   *b);
void    push_to_heap(t_pqueue  *q, int coder_id, long  priority_score);
void    pop_from_heap(t_pqueue  *q);

long    get_time_ms(void);
void    smart_sleep(t_hub   *hub, long  duration_ms);
void    print_state(t_hub   *hub, int   id, char    *state);
int is_num_str(const char   *str);

void    *coder_routine(void *arg);
void    acq_single_d(t_coder    *coder, t_dongle    *dongle);
void    rel_single_d(t_coder   *coder, t_dongle    *dongle);

void    *monitor_routine(void   *arg);
void    wake_all_coders(t_hub  *hub);

int val_args(int    argc, char  **argv);
int init_hub(t_hub  *hub, int   argc, char  **argv);

#endif