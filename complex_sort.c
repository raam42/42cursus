/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   complex_sort.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandres <roandres@student.42madrid.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/29 22:54:56 by roandres          #+#    #+#             */
/*   Updated: 2026/04/29 22:54:56 by roandres         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static int    get_max_index(t_stack_node *a)
{
    int    max;

    if (!a)
        return (0);
    max = a->index;
    while (a)
    {
        if (a->index > max)
            max = a->index;
        a = a->next;
    }
    return (max);
}

static int    get_max_bits(int max_index)
{
    int    bits;

    bits = 0;
    while ((max_index >> bits) != 0)
        bits++;
    return (bits);
}

static void    push_back_all(t_stack_node **a, t_stack_node **b)
{
    while (*b)
        pa(a, b, 0);
}

void    complex_sort(t_stack_node **a, t_stack_node **b)
{
    int    size;
    int    bit;
    int    bits;
    int    i;

    if (!a || !*a || stack_sorted(*a))
        return ;
    size = len_stack(*a);
    bits = get_max_bits(get_max_index(*a));
    bit = 0;
    while (bit < bits)
    {
        i = 0;
        while (i++ < size)
        {
            if ((((*a)->index >> bit) & 1) == 0)
                pb(a, b, 0);
            else
                ra(a, 0);
        }
        push_back_all(a, b);
        if (stack_sorted(*a))
            return ;
        bit++;
    }
}
