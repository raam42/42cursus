/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   checker.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandres <roandres@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/04 03:00:00 by roandres          #+#    #+#             */
/*   Updated: 2026/05/04 03:00:00 by roandres         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"
#include "gnl/get_next_line.h"

static int	ft_strcmp(const char *s1, const char *s2)
{
	size_t	i;

	i = 0;
	while (s1[i] && s2[i] && s1[i] == s2[i])
		i++;
	return ((unsigned char)s1[i] - (unsigned char)s2[i]);
}

static void	execute_instruction(t_stack_node **a, t_stack_node **b, char *line)
{
	if (ft_strcmp(line, "sa\n") == 0)
		sa(a, 1);
	else if (ft_strcmp(line, "sb\n") == 0)
		sb(b, 1);
	else if (ft_strcmp(line, "ss\n") == 0)
		ss(a, b, 1);
	else if (ft_strcmp(line, "pa\n") == 0)
		pa(a, b, 1);
	else if (ft_strcmp(line, "pb\n") == 0)
		pb(a, b, 1);
	else if (ft_strcmp(line, "ra\n") == 0)
		ra(a, 1);
	else if (ft_strcmp(line, "rb\n") == 0)
		rb(b, 1);
	else if (ft_strcmp(line, "rr\n") == 0)
		rr(a, b, 1);
	else if (ft_strcmp(line, "rra\n") == 0)
		rra(a, 1);
	else if (ft_strcmp(line, "rrb\n") == 0)
		rrb(b, 1);
	else if (ft_strcmp(line, "rrr\n") == 0)
		rrr(a, b, 1);
	else
	{
		free(line);
		ft_putstr_fd("Error\n", 2);
		free_stack(*a);
		free_stack(*b);
		exit(1);
	}
}

int	main(int argc, char **argv)
{
	t_stack_node	*a;
	t_stack_node	*b;
	t_ctx			ctx;
	char			*line;
	int				res;
	int				sorted;

	if (argc < 2)
		return (0);
	ctx.strategy = ADAPTIVE;
	ctx.bench = 0;
	ctx.start_idx = 1;
	ft_bzero(&ctx.b, sizeof(t_bench));
	res = parse_flags(argv, &ctx);
	if (res == 0)
	{
		ft_putstr_fd("Error\n", 2);
		return (1);
	}
	if (ctx.start_idx >= argc)
		return (0);
	a = parse_and_fill_stack(argc, argv, ctx.start_idx, &ctx);
	if (!a)
	{
		ft_putstr_fd("Error\n", 2);
		return (1);
	}
	set_node_index(a);
	b = NULL;
	line = get_next_line(STDIN_FILENO);
	while (line)
	{
		execute_instruction(&a, &b, line);
		free(line);
		line = get_next_line(STDIN_FILENO);
	}
	sorted = stack_sorted(a);
	if (sorted && !b)
		ft_putstr("OK\n");
	else
		ft_putstr("KO\n");
	free_stack(a);
	free_stack(b);
	return (0);
}
