#include "push_swap.h"

/*
** Adaptive strategy selector
** Chooses the appropriate internal algorithm based on the disorder index.
** This function performs NO sorting logic itself — it only dispatches.
*/
static void    run_adaptive(t_stack_node **a, t_stack_node **b, t_ctx *ctx)
{
    float    disorder;

    disorder = compute_disorder(*a);
    if (disorder < 0.2f)
    {
        if (ctx->bench)
            ctx->b.used_strategy = SIMPLE;
        simple_sort(a, b);
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
}

/*
** Main strategy dispatcher
** Selects the strategy based on command-line flags.
** --adaptive is the default when no strategy flag is provided.
*/
void    run_strategy(t_stack_node **a, t_stack_node **b, t_ctx *ctx)
{
    if (ctx->bench)
        ctx->b.used_strategy = ctx->strategy;

    if (ctx->strategy == SIMPLE)
        simple_sort(a, b);
    else if (ctx->strategy == MEDIUM)
        medium_sort(a, b);
    else if (ctx->strategy == COMPLEX)
        complex_sort(a, b);
    else
        run_adaptive(a, b, ctx);
}
