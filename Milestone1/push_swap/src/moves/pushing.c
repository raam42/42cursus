/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   pushing.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandres <roandres@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/25 20:10:40 by roandres          #+#    #+#             */
/*   Updated: 2026/04/29 15:10:34 by roandres         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	push(t_stack_node **to, t_stack_node **from)
{
	t_stack_node	*to_push;

	if (!*from)
		return ;
	to_push = *from;
	*from = (*from)->next;
	if (*from)
		(*from)->prev = NULL;
	to_push->prev = NULL;
	if (!*to)
	{
		*to = to_push;
		to_push->next = NULL;
	}
	else
	{
		to_push->next = *to;
		(*to)->prev = to_push;
		*to = to_push;
	}
}

void	pa(t_stack_node **stack_a, t_stack_node **stack_b, int testing)
{
	push(stack_a, stack_b);
	if (!testing)
	{
		if (*stack_a && (*stack_a)->ctx && (*stack_a)->ctx->bench)
		{
			(*stack_a)->ctx->b.pa++;
			(*stack_a)->ctx->b.total++;
		}
		ft_putstr("pa\n");
	}
}

void	pb(t_stack_node **stack_a, t_stack_node **stack_b, int testing)
{
	push(stack_b, stack_a);
	if (!testing)
	{
		if (*stack_b && (*stack_b)->ctx && (*stack_b)->ctx->bench)
		{
			(*stack_b)->ctx->b.pb++;
			(*stack_b)->ctx->b.total++;
		}
		ft_putstr("pb\n");
	}
}
