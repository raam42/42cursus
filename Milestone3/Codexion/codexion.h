/* ************************************************************************* */
/*                                                                           */
/*                                                       :::      ::::::::   */
/*   codexion.h                                        :+:      :+:    :+:   */
/*                                                   +:+ +:+         +:+     */
/*   By: rodrigoa <rodrigoa@student.42madrid.com>  +#+  +:+       +#+        */
/*                                               +#+#+#+#+#+   +#+           */
/*   Created: 2026/10/28 19:25:13 by rodrigoa         #+#    #+#             */
/*   Updated: 2026/10/28 19:25:16 by rodrigoa        ###   ########.fr       */
/*                                                                           */
/* ************************************************************************* */
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
    POLICY_FIFO,
    POLICY_EDF
}   t_scheduler;


typedef struct s_request
{
    int coder_id;
    long    p_score;
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
    long    last_compile_start;
    int compiles_done;
    t_dongle    *left_dongle;
    t_dongle    *right_dongle;
    t_hub   *hub;
}   t_coder;


struct  s_hub
{
    int num_coders;
    long    time_to_burnout;
    long    time_to_compile;
    long    time_to_debug;
    long    time_to_refactor;
    int required_compiles;
    long    dongle_cooldown;
    t_scheduler scheduler;

    long    start_time;
    int simulation_active;

    pthread_mutex_t write_lock;
    pthread_mutex_t state_lock;

    t_dongle    *dongles;
    t_coder *coders;
};


void    swap_requests(t_request    *a, t_request   *b);
void    push_to_heap(t_pqueue  *q, int coder_id, long  p_score);
void    pop_from_heap(t_pqueue  *q);

long    get_time_ms(void);
void    wake_all_coders(t_hub  *hub);
void    smart_sleep(t_hub   *hub, long  duration_ms);
void    print_state(t_hub   *hub, int   id, char    *state);

void    *monitor_routine(void   *arg);

void    acq_single_d(t_coder    *coder, t_dongle    *dongle);
void    rel_single_d(t_coder   *coder, t_dongle    *dongle);
void    *coder_routine(void *arg);

int is_num_str(const char   *str);
int val_args(int    argc, char  **argv);
int init_hub(t_hub  *hub, char  **argv);

#endif
