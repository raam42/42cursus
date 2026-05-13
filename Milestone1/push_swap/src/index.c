/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   index.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandres <roandres@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/31 17:12:56 by roandres          #+#    #+#             */
/*   Updated: 2026/03/31 17:14:54 by roandres         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	set_node_index(t_stack_node *stack)
{
	t_stack_node	*current;
	t_stack_node	*compare;
	int				count;

	current = stack;
	while (current)
	{
		count = 0;
		compare = stack;
		while (compare)
		{
			if (compare->value < current->value)
				count++;
			compare = compare->next;
		}
		current->index = count;
		current = current->next;
	}
}
