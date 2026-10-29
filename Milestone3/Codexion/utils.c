/* ************************************************************************* */
/*                                                                           */
/*                                                       :::      ::::::::   */
/*   utils.c                                           :+:      :+:    :+:   */
/*                                                   +:+ +:+         +:+     */
/*   By: rodrigoa <rodrigoa@student.42madrid.com>  +#+  +:+       +#+        */
/*                                               +#+#+#+#+#+   +#+           */
/*   Created: 2026/10/28 19:21:48 by rodrigoa         #+#    #+#             */
/*   Updated: 2026/10/28 20:32:35 by rodrigoa        ###   ########.fr       */
/*                                                                           */
/* ************************************************************************* */
#include "codexion.h"

void    smart_sleep(t_hub*hub, long duration_ms)
{
    long    start_time;
    int active;

    start_time = get_time_ms();
    while (1)
    {
        pthread_mutex_lock(&hub->state_lock);
        active = hub->simulation_active;
        pthread_mutex_unlock(&hub->state_lock);
        if (!active || get_time_ms() - start_time >= duration_ms)
            break;
        usleep(500);
    }
}

void    print_state(t_hub   *hub, int   id, char    *state)
{
    pthread_mutex_lock(&hub->state_lock);
    if (hub->simulation_active)
    {
        pthread_mutex_lock(&hub->write_lock);
        printf ("%ld %d %s\n", get_time_ms() - hub->start_time, id, state);
        pthread_mutex_unlock(&hub->write_lock);
    }
    pthread_mutex_unlock(&hub->state_lock);
}

void    wake_all_coders(t_hub   *hub)
{
    int i;

    i = 0;
    while (i < hub->num_coders)
    {
        pthread_mutex_lock(&hub->dongles[i].lock);
        pthread_cond_broadcast(&hub->dongles[i].cv);
        pthread_mutex_unlock(&hub->dongles[i].lock);
        i++;
    }
}

static int  check_burnout(t_hub *hub, int i)
{
    long    current_time;

    current_time = get_time_ms();
    if (current_time - hub->coders[i].last_compile_start \
        >= hub->time_to_burnout)
    {
        pthread_mutex_lock(&hub->write_lock);
        printf ("%ld %d burned out\n", current_time - hub->start_time, \
                hub->coders[i].id);
        hub->simulation_active = 0;
        pthread_mutex_unlock(&hub->write_lock);
        pthread_mutex_unlock(&hub->state_lock);
        wake_all_coders(hub);
        return (1);
    }
    return (0);
}

void    *monitor_routine(void *arg)
{
    t_hub   *hub;
    int i;
    int finished;

    hub = (t_hub    *)arg;
    while (1)
    {
        finished = 0;
        i = 0;
        pthread_mutex_lock(&hub->state_lock);
        while (i < hub->num_coders)
        {
            if (check_burnout(hub, i))
                return (NULL);
            if (hub->required_compiles > 0 && \
                hub->coders[i].compiles_done >= hub->required_compiles)
                finished++;
            i++;
        }
        if (hub->required_compiles > 0 && finished == hub->num_coders)
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
