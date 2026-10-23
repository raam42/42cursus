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
    
}