/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   rotating.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandres <roandres@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/25 20:10:36 by roandres          #+#    #+#             */
/*   Updated: 2026/04/29 15:04:02 by roandres         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	ft_rotate_node(t_stack_node **stack)
{
	t_stack_node	*first;
	t_stack_node	*last;

	if (!*stack || !(*stack)->next)
		return ;
	first = *stack;
	last = last_node(*stack);
	*stack = first->next;
	(*stack)->prev = NULL;
	last->next = first;
	first->prev = last;
	first->next = NULL;
}

void	ra(t_stack_node **stack_a, int testing)
{
	ft_rotate_node(stack_a);
	if (!testing)
	{
		if (*stack_a && (*stack_a)->ctx && (*stack_a)->ctx->bench)
		{
			(*stack_a)->ctx->b.ra++;
			(*stack_a)->ctx->b.total++;
		}
		ft_putstr("ra\n");
	}
}

void	rb(t_stack_node **stack_b, int testing)
{
	ft_rotate_node(stack_b);
	if (!testing)
	{
		if (*stack_b && (*stack_b)->ctx && (*stack_b)->ctx->bench)
		{
			(*stack_b)->ctx->b.rb++;
			(*stack_b)->ctx->b.total++;
		}
		ft_putstr("rb\n");
	}
}

void	rr(t_stack_node **stack_a, t_stack_node **stack_b, int testing)
{
	ft_rotate_node(stack_a);
	ft_rotate_node(stack_b);
	if (!testing)
	{
		if (*stack_a && (*stack_a)->ctx && (*stack_a)->ctx->bench)
		{
			(*stack_a)->ctx->b.rr++;
			(*stack_a)->ctx->b.total++;
		}
		else if (*stack_b && (*stack_b)->ctx && (*stack_b)->ctx->bench)
		{
			(*stack_b)->ctx->b.rr++;
			(*stack_b)->ctx->b.total++;
		}
		ft_putstr("rr\n");
	}
}
