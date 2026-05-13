/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   stack_mngr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandres <roandres@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/25 20:52:01 by roandres          #+#    #+#             */
/*   Updated: 2026/04/16 20:12:09 by roandres         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	ft_putstr(char *str)
{
	while (*str)
		write(1, str++, 1);
}

int	len_stack(t_stack_node *stack)
{
	int	i;

	i = 0;
	if (!stack)
		return (0);
	while (stack)
	{
		stack = stack->next;
		i++;
	}
	return (i);
}

int	stack_sorted(t_stack_node *stack)
{
	if (!stack)
		return (1);
	while (stack->next)
	{
		if (stack->value > stack->next->value)
			return (0);
		stack = stack->next;
	}
	return (1);
}

t_stack_node	*find_min_node(t_stack_node *stack)
{
	t_stack_node	*min_node;
	long			min_value;

	min_value = LONG_MAX;
	if (!stack)
		return (NULL);
	while (stack)
	{
		if (stack->value < min_value)
		{
			min_node = stack;
			min_value = stack->value;
		}
		stack = stack->next;
	}
	return (min_node);
}

t_stack_node	*find_max_node(t_stack_node *stack)
{
	t_stack_node	*max_node;
	long			max_value;

	max_value = LONG_MIN;
	if (!stack)
		return (NULL);
	while (stack)
	{
		if (stack->value > max_value)
		{
			max_node = stack;
			max_value = stack->value;
		}
		stack = stack->next;
	}
	return (max_node);
}
