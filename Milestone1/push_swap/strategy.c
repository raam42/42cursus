/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   strategy.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandres <roandres@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/22 11:56:03 by roandres          #+#    #+#             */
/*   Updated: 2026/04/27 19:28:53 by roandres         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static void	run_adaptive(t_stack_node **a, t_stack_node **b, t_ctx *ctx)
{
	float	disorder;

	disorder = compute_disorder(*a);
	if (disorder < 0.2f)
	{
		if (ctx->bench)
			ctx->b.used_strategy = LINEAR;
 		if (!linear_sort(a))
    	{
        	if (ctx->bench)
            	ctx->b.used_strategy = MEDIUM;
        	medium_sort(a, b);
    	}
		linear_sort(a);
	}
	else if (disorder < 0.5f)
	{
		if (ctx->bench)
			ctx->b.used_strategy = MEDIUM;
		medium_sort(a, b);
	}
	else
	{
		if (ctx->bench)
			ctx->b.used_strategy = COMPLEX;
		complex_sort(a, b);
	}
	(void)ctx;
}

void	run_strategy(t_stack_node **a, t_stack_node **b, t_ctx *ctx)
{
	if (ctx->strategy == SIMPLE)
	{
		if (ctx->bench)
            ctx->b.used_strategy = SIMPLE;
		simple_sort(a, b);
	}
	else if (ctx->strategy == MEDIUM)
	{
		if (ctx->bench)
            ctx->b.used_strategy = MEDIUM;
		medium_sort(a, b);
	}
	else if (ctx->strategy == COMPLEX)
	{
		if (ctx->bench)
            ctx->b.used_strategy = COMPLEX;
		complex_sort(a, b);
	}
	else
		run_adaptive(a, b, ctx);
}
