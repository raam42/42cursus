/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   complex_sort.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: you <you@student.42madrid.com>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/29                                  #+#    #+#         */
/*   Updated: 2026/04/29                                  ###   ########.fr   */
/*                                                                            */
/* ************************************************************************** */

/*
** ADAPT 1/3: include your project header
*/
#include "push_swap.h"

/*
** ADAPT 2/3: these types/fields must match your project.
** Common patterns:
** - t_stack holds pointer to top (head) node: stack->top or stack->head
** - t_node has: int index; t_node *next;
*/
static int    ps_stack_size(t_stack *s)
{
    int        n;
    t_node    *cur;

    n = 0;
    cur = NULL;
    if (!s)
        return (0);
    cur = s->top;
    while (cur)
    {
        n++;
        cur = cur->next;
    }
    return (n);
}

static int    ps_is_sorted(t_stack *a)
{
    t_node    *cur;

    if (!a || !a->top)
        return (1);
    cur = a->top;
    while (cur && cur->next)
    {
        if (cur->index > cur->next->index)
            return (0);
        cur = cur->next;
    }
    return (1);
}

static int    ps_max_index(t_stack *a)
{
    int        max;
    t_node    *cur;

    max = 0;
    cur = NULL;
    if (!a || !a->top)
        return (0);
    cur = a->top;
    max = cur->index;
    while (cur)
    {
        if (cur->index > max)
            max = cur->index;
        cur = cur->next;
    }
    return (max);
}

static int    ps_max_bits(int max_index)
{
    int    bits;

    bits = 0;
    while ((max_index >> bits) != 0)
        bits++;
    return (bits);
}

/*
** ADAPT 3/3: map these calls to your move functions.
** I assume prototypes like:
**   void pb(t_stack *a, t_stack *b);
** If yours are pointers (t_stack **), adjust accordingly.
*/
static void    ps_push_back_all(t_stack *a, t_stack *b)
{
    while (b && b->top)
        pa(a, b);
}

static void    ps_radix_pass(t_stack *a, t_stack *b, int bit, int size)
{
    int    i;
    int    top_i;

    i = 0;
    while (i < size)
    {
        top_i = a->top->index;
        if (((top_i >> bit) & 1) == 0)
            pb(a, b);
        else
            ra(a);
        i++;
    }
    ps_push_back_all(a, b);
}

/*
** Public entry point: call this for 500+ (or generally for "big sort").
*/
void    complex_sort(t_stack *a, t_stack *b)
{
    int    size;
    int    bit;
    int    bits;

    if (!a || ps_is_sorted(a))
        return ;
    size = ps_stack_size(a);
    bits = ps_max_bits(ps_max_index(a));
    bit = 0;
    while (bit < bits)
    {
        ps_radix_pass(a, b, bit, size);
        if (ps_is_sorted(a))
            return ;
        bit++;
    }
}
``
