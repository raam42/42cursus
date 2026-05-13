/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   flags.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandres <roandres@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/22 12:01:36 by roandres          #+#    #+#             */
/*   Updated: 2026/04/27 19:46:35 by roandres         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static int	check_strat(char *arg, t_strategy *strat)
{
	if (!ft_strncmp(arg, "--simple", 9))
		*strat = SIMPLE;
	else if (!ft_strncmp(arg, "--medium", 9))
		*strat = MEDIUM;
	else if (!ft_strncmp(arg, "--complex", 10))
		*strat = COMPLEX;
	else if (!ft_strncmp(arg, "--adaptive", 11))
		*strat = ADAPTIVE;
	else
		return (0);
	return (1);
}

int	parse_flags(char **argv, t_ctx *ctx)
{
	int	s_set;

	s_set = 0;
	while (argv[ctx->start_idx])
	{
		if (!ft_strncmp(argv[ctx->start_idx], "--bench", 8))
			ctx->bench = 1;
		else if (check_strat(argv[ctx->start_idx], &ctx->strategy))
		{
			if (s_set)
				return (0);
			s_set = 1;
		}
		else if (!ft_strncmp(argv[ctx->start_idx], "--", 2))
			return (0);
		else
			break ;
		ctx->start_idx++;
	}
	return (1);
}

int	init_ctx(int argc, char **argv, t_ctx *ctx)
{
	if (argc < 2)
		return (0);
	ctx->strategy = ADAPTIVE;
	ctx->bench = 0;
	ctx->start_idx = 1;
	ft_bzero(&ctx->b, sizeof(t_bench));
	if (!parse_flags(argv, ctx))
		return (-1);
	if (ctx->start_idx >= argc)
		return (0);
	return (1);
}
