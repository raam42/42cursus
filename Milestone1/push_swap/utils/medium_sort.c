/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   medium_sort.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandres <roandres@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/14 21:40:41 by roandres          #+#    #+#             */
/*   Updated: 2026/04/21 11:39:06 by roandres         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static int	ft_isqrt(int n)
{
	int	i;

	i = 1;
	if (n <= 0)
		return (0);
	while ((i * i) <= n && i < 46341)
		i++;
	return (i - 1);
}

static int	get_max_index_pos(t_stack_node *stack)
{
	int	pos;
	int	best_pos;
	int	best_idx;

	pos = 0;
	best_pos = 0;
	best_idx = -1;
	while (stack)
	{
		if (stack->index > best_idx)
		{
			best_idx = stack->index;
			best_pos = pos;
		}
		pos++;
		stack = stack->next;
	}
	return (best_pos);
}

static void	push_chunks_to_b(t_stack_node **a, t_stack_node **b, int chunk)
{
	int	i;

	i = 0;
	while (*a)
	{
		if ((*a)->index <= i)
		{
			pb(a, b, 0);
			rb(b, 0);
			i++;
		}
		else if ((*a)->index <= (i + chunk))
		{
			pb(a, b, 0);
			i++;
		}
		else
			ra(a, 0);
	}
}

static void	push_back_to_a(t_stack_node **a, t_stack_node **b)
{
	int	size;
	int	pos;

	while (*b)
	{
		size = len_stack(*b);
		pos = get_max_index_pos(*b);
		if (pos <= (size / 2))
		{
			while (pos > 0)
			{
				rb(b, 0);
				pos--;
			}
		}
		else
		{
			pos = size - pos;
			while (pos-- > 0)
				rrb(b, 0);
		}
		pa(a, b, 0);
	}
}

void	medium_sort(t_stack_node **a, t_stack_node **b)
{
	int	size;
	int	chunk;

	size = len_stack(*a);
	if (size <= 1)
		return ;
	chunk = ft_isqrt(size);
	if (chunk < 5)
		chunk = 5;
	push_chunks_to_b(a, b, chunk);
	push_back_to_a(a, b);
}
