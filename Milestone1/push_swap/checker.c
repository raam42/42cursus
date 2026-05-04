#include "push_swap.h"

static int    exec_instruction(char *line,
                             t_stack_node **a,
                             t_stack_node **b)
{
    if (!ft_strncmp(line, "sa\n", 3))
        return (sa(a, 1), 1);
    if (!ft_strncmp(line, "sb\n", 3))
        return (sb(b, 1), 1);
    if (!ft_strncmp(line, "ss\n", 3))
        return (ss(a, b, 1), 1);
    if (!ft_strncmp(line, "pa\n", 3))
        return (pa(a, b, 1), 1);
    if (!ft_strncmp(line, "pb\n", 3))
        return (pb(a, b, 1), 1);
    if (!ft_strncmp(line, "ra\n", 3))
        return (ra(a, 1), 1);
    if (!ft_strncmp(line, "rb\n", 3))
        return (rb(b, 1), 1);
    if (!ft_strncmp(line, "rr\n", 3))
        return (rr(a, b, 1), 1);
    if (!ft_strncmp(line, "rra\n", 4))
        return (rra(a, 1), 1);
    if (!ft_strncmp(line, "rrb\n", 4))
        return (rrb(b, 1), 1);
    if (!ft_strncmp(line, "rrr\n", 4))
        return (rrr(a, b, 1), 1);
    return (0);
}

static void    free_and_error(t_stack_node *a, t_stack_node *b)
{
    free_stack(a);
    free_stack(b);
    write(2, "Error\n", 6);
}

int    main(int argc, char **argv)
{
    t_stack_node    *a;
    t_stack_node    *b;
    t_ctx            ctx;
    char            *line;

    if (argc < 2)
        return (0);
    if (init_ctx(argc, argv, &ctx) < 0)
        return (write(2, "Error\n", 6), 1);
    a = parse_and_fill_stack(argc, argv, ctx.start_idx, &ctx);
    if (!a)
        return (write(2, "Error\n", 6), 1);
    b = NULL;
    line = get_next_line(0);
    while (line)
    {
        if (!exec_instruction(line, &a, &b))
            return (free(line), free_and_error(a, b), 1);
        free(line);
        line = get_next_line(0);
    }
    if (stack_sorted(a) && !b)
        write(1, "OK\n", 3);
    else
        write(1, "KO\n", 3);
    free_stack(a);
    free_stack(b);
    return (0);
}
