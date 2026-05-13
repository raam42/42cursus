/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   complex_sort.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandres <roandres@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/10 13:21:31 by rodrigoa          #+#    #+#             */
/*   Updated: 2026/05/01 14:17:12 by roandres         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static int	get_max_bits(t_stack_node *a)
{
	int	max;
	int	bits;

	max = len_stack(a) - 1;
	bits = 0;
	while ((max >> bits) != 0)
		bits++;
	return (bits);
}

static void	sort_bit_pass(t_stack_node **a, t_stack_node **b, int bit)
{
	int	size;
	int	i;

	size = len_stack(*a);
	i = 0;
	while (i < size)
	{
		if ((((*a)->index >> bit) & 1) == 1)
			ra(a, 0);
		else
			pb(a, b, 0);
		i++;
	}
}

static void	restore_stack(t_stack_node **a, t_stack_node **b)
{
	while (*b)
		pa(a, b, 0);
}

void	complex_sort(t_stack_node **a, t_stack_node **b)
{
	int	bits;
	int	i;

	if (!a || !*a || stack_sorted(*a))
		return ;
	bits = get_max_bits(*a);
	i = 0;
	while (i < bits)
	{
		sort_bit_pass(a, b, i);
		restore_stack(a, b);
		i++;
	}
}
