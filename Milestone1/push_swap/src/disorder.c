/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   disorder.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandres <roandres@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/31 17:15:36 by roandres          #+#    #+#             */
/*   Updated: 2026/04/16 20:11:23 by roandres         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

// Calculates the disorder index of the stack (between 0.0 and 1.0)
float	compute_disorder(t_stack_node *stack)
{
	t_stack_node	*current;
	t_stack_node	*compare;
	int				mistakes;
	int				total_pairs;

	mistakes = 0;
	total_pairs = 0;
	current = stack;
	while (current)
	{
		compare = current->next;
		while (compare)
		{
			total_pairs++;
			if (current->value > compare->value)
				mistakes++;
			compare = compare->next;
		}
		current = current->next;
	}
	if (total_pairs == 0)
		return (0.0f);
	return ((float)mistakes / (float)total_pairs);
}
