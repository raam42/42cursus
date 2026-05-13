#include "push_swap.h"

static void	run_adaptive(t_stack_node **a, t_stack_node **b, t_ctx *ctx)
{
	float	disorder;

	disorder = compute_disorder(*a);
	if (disorder < 0.2f)
	{
		if (!linear_sort(a))
			medium_sort(a, b);
	}
	else if (disorder < 0.5f)
		medium_sort(a, b);
	else
		complex_sort(a, b);
	(void)ctx;
}

void	run_strategy(t_stack_node **a, t_stack_node **b, t_ctx *ctx)
{
	if (ctx->strategy == SIMPLE)
		simple_sort(a, b);
	else if (ctx->strategy == MEDIUM)
		medium_sort(a, b);
	else if (ctx->strategy == COMPLEX)
		complex_sort(a, b);
	else
		run_adaptive(a, b, ctx);
}
