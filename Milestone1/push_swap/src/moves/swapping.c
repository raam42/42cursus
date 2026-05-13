/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   swapping.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandres <roandres@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/25 14:20:18 by roandres          #+#    #+#             */
/*   Updated: 2026/04/29 15:11:48 by roandres         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	ft_swap_nodes(t_stack_node **head)
{
	t_stack_node	*first;
	t_stack_node	*second;

	if (!*head || !(*head)->next)
		return ;
	first = *head;
	second = (*head)->next;
	first->next = second->next;
	if (second->next)
		second->next->prev = first;
	second->prev = first->prev;
	second->next = first;
	first->prev = second;
	*head = second;
}

void	sa(t_stack_node **stack_a, int testing)
{
	ft_swap_nodes(stack_a);
	if (!testing)
	{
		if (*stack_a && (*stack_a)->ctx && (*stack_a)->ctx->bench)
		{
			(*stack_a)->ctx->b.sa++;
			(*stack_a)->ctx->b.total++;
		}
		ft_putstr("sa\n");
	}
}

void	sb(t_stack_node **stack_b, int testing)
{
	ft_swap_nodes(stack_b);
	if (!testing)
	{
		if (*stack_b && (*stack_b)->ctx && (*stack_b)->ctx->bench)
		{
			(*stack_b)->ctx->b.sb++;
			(*stack_b)->ctx->b.total++;
		}
		ft_putstr("sb\n");
	}
}

void	ss(t_stack_node **stack_a, t_stack_node **stack_b, int testing)
{
	ft_swap_nodes(stack_a);
	ft_swap_nodes(stack_b);
	if (!testing)
	{
		if (*stack_a && (*stack_a)->ctx && (*stack_a)->ctx->bench)
		{
			(*stack_a)->ctx->b.ss++;
			(*stack_a)->ctx->b.total++;
		}
		else if (*stack_b && (*stack_b)->ctx && (*stack_b)->ctx->bench)
		{
			(*stack_b)->ctx->b.ss++;
			(*stack_b)->ctx->b.total++;
		}
		ft_putstr("ss\n");
	}
}
