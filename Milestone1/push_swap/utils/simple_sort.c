/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   simple_sort.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandres <roandres@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/06 11:36:35 by roandres          #+#    #+#             */
/*   Updated: 2026/04/27 19:01:11 by roandres         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static int	get_min_pos(t_stack_node *stack)
{
	int	min_idx;
	int	min_pos;
	int	current_pos;

	min_idx = INT_MAX;
	min_pos = 0;
	current_pos = 0;
	while (stack)
	{
		if (stack->index < min_idx)
		{
			min_idx = stack->index;
			min_pos = current_pos;
		}
		current_pos++;
		stack = stack->next;
	}
	return (min_pos);
}

void	simple_sort(t_stack_node **a, t_stack_node **b)
{
	int	size;
	int	min_pos;

	size = len_stack(*a);
	while (size > 0)
	{
		min_pos = get_min_pos(*a);
		if (min_pos <= size / 2)
		{
			while (min_pos-- > 0)
				ra(a, 0);
		}
		else
		{
			min_pos = size - min_pos;
			while (min_pos-- > 0)
				rra(a, 0);
		}
		pb(a, b, 0);
		size--;
	}
	while (*b)
		pa(a, b, 0);
}
