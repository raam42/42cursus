#include "push_swap.h"

static void    linear_pass(t_stack_node **a, int size)
{
    int    i;

    i = 0;
    while (i < size)
    {
        if ((*a)->next && (*a)->value > (*a)->next->value)
            sa(a, 0);
        ra(a, 0);
        i++;
    }
}

int    linear_sort(t_stack_node **a)
{
    int    size;
    int    pass;

    if (!a || !*a || stack_sorted(*a))
        return (1);
    size = len_stack(*a);
    pass = 0;
    while (pass < 2)
    {
        linear_pass(a, size);
        if (stack_sorted(*a))
            return (1);
        pass++;
    }
    return (0);
}
