/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   parser.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandres <roandres@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/19 17:18:31 by roandres          #+#    #+#             */
/*   Updated: 2026/04/29 14:20:51 by roandres         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

int	is_valid_number(const char *str)
{
	int	i;

	i = 0;
	if (str[i] == '+' || str[i] == '-')
		i++;
	if (str[i] == '\0')
		return (0);
	while (str[i])
	{
		if (!ft_isdigit(str[i]))
			return (0);
		i++;
	}
	return (1);
}

int	check_duplicate(t_stack_node *stack, int num)
{
	while (stack)
	{
		if (stack->value == num)
			return (1);
		stack = stack->next;
	}
	return (0);
}

void	add_to_stack(t_stack_node **stack, int num, t_ctx *ctx)
{
	t_stack_node	*new_node;
	t_stack_node	*last;

	new_node = malloc(sizeof(t_stack_node));
	if (!new_node)
		return ;
	new_node->value = num;
	new_node->index = -1;
	new_node->ctx = ctx;
	new_node->next = NULL;
	if (!*stack)
	{
		new_node->prev = NULL;
		*stack = new_node;
	}
	else
	{
		last = last_node(*stack);
		last->next = new_node;
		new_node->prev = last;
	}
}

static int	split_args(char **args, t_stack_node **stack, t_ctx *ctx)
{
	int	i;
	int	num;

	i = 0;
	while (args[i])
	{
		if (!is_valid_number(args[i]) || !ft_safe_atoi(args[i], &num)
			|| check_duplicate(*stack, num))
			return (0);
		add_to_stack(stack, num, ctx);
		i++;
	}
	return (1);
}

t_stack_node	*parse_and_fill_stack(int argc, char **argv, int start_idx,
									t_ctx *ctx)
{
	t_stack_node	*stack;
	char			**splited;
	int				i;

	stack = NULL;
	i = start_idx;
	while (i < argc)
	{
		splited = ft_split(argv[i], ' ');
		if (!splited || !split_args(splited, &stack, ctx))
		{
			free_split(splited);
			free_stack(stack);
			return (NULL);
		}
		free_split(splited);
		i++;
	}
	return (stack);
}
