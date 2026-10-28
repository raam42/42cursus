/* ************************************************************************* */
/*                                                                           */
/*                                                       :::      ::::::::   */
/*   coder_routine.c                                   :+:      :+:    :+:   */
/*                                                   +:+ +:+         +:+     */
/*   By: rodrigoa <rodrigoa@student.42madrid.com>  +#+  +:+       +#+        */
/*                                               +#+#+#+#+#+   +#+           */
/*   Created: 2026/10/28 19:03:15 by rodrigoa         #+#    #+#             */
/*   Updated: 2026/10/28 19:17:51 by rodrigoa        ###   ########.fr       */
/*                                                                           */
/* ************************************************************************* */
#include "codexion.h"

static void wait_for_dongle(t_coder *coder, t_dongle    *dongle)
{
    while (coder->hub->simulation_active)
    {
        if (dongle->is_held || dongle->queue.requests[0].coder_id != coder->id)
            pthread_cond_wait(&dongle->cv, &dongle->lock);
        else if (get_time_ms() < dongle->available_at)
        {
            pthread_mutex_unlock(&dongle->lock);
            usleep(500);
            pthread_mutex_lock(&dongle->lock);
        }
        else
            break;
    }
}

void    acq_single_d(t_coder    *coder, t_dongle    *dongle)
{
    long    p_score;
    
    pthread_mutex_lock(&dongle->lock);
    if (coder->hub->scheduler == POLICY_FIFO)
        p_score = get_time_ms();
    else
        p_score = coder->last_compile_start + coder->hub->time_to_burnout;
    push_to_heap(&dongle->queue, coder->id, p_score);
    wait_for_dongle(coder, dongle);
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

static int  perform_compile(t_coder *coder, t_dongle    *d1, t_dongle   *d2)
{
    int active;

    acq_single_d(coder, d1);
    pthread_mutex_lock(&coder->hub->state_lock);
    active = coder->hub->simulation_active;
    pthread_mutex_unlock(&coder->hub->state_lock);
    if (!active)
        return (0);
    acq_single_d(coder, d2);
    pthread_mutex_lock(&coder->hub->state_lock);
    active = coder->hub->simulation_active;
    pthread_mutex_unlock(&coder->hub->state_lock);
    if (!active)
        return (0);
    pthread_mutex_lock(&coder->hub->state_lock);
    coder->last_compile_start = get_time_ms();
    coder->compiles_done++;
    pthread_mutex_unlock(&coder->hub->state_lock);
    print_state(coder->hub, coder->id, "is compiling");
    smart_sleep(coder->hub, coder->hub->time_to_compile);
    rel_single_d(coder, d1);
    rel_single_d(coder, d2);
    return (1);
}

void    *coder_routine(void *arg)
{
    t_coder *coder;
    t_dongle    *d1;
    t_dongle    *d2;

    coder = (t_coder    *)arg;
    d1 = coder->left_dongle;
    d2 = coder->right_dongle;
    if (coder->id % 2 != 0)
    {
        d1 = coder->right_dongle;
        d2 = coder->left_dongle;
    }
    while (1)
    {
        if (!perform_compile(coder, d1, d2))
            break;
        if (coder->hub->required_compiles > 0 && \
            coder->compiles_done >= coder->hub->required_compiles)
          break;
        print_state(coder->hub, coder->id, "is debugging");
        smart_sleep(coder->hub, coder->hub->time_to_debug);
        print_state(coder->hub, coder->id, "is refactoring");
        smart_sleep(coder->hub, coder->hub->time_to_refactor);
    }
    return (NULL);
}
