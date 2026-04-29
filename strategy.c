#include "push_swap.h"

/*
** Adaptive strategy selector
** Decides which internal strategy to use based on disorder index.
** This function NEVER performs moves directly.
*/
static void    run_adaptive(t_stack_node **a, t_stack_node **b, t_ctx *ctx)
{
    float    disorder;

    (void)ctx;
    disorder = compute_disorder(*a);
    if (disorder < 0.2f)
    {
        /*
        ** Low disorder → near-sorted input
        ** Required complexity: O(n)
        */
        simple_sort(a, b);
    }
    else if (disorder < 0.5f)
    {
        /*
        ** Medium disorder
        ** Required complexity: O(n√n)
        */
        medium_sort(a, b);
    }
    else
    {
        /*
        ** High disorder
        ** Required complexity: O(n log n)
        */
        complex_sort(a, b);
    }
}

void    run_strategy(t_stack_node **a, t_stack_node **b, t_ctx *ctx)
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
