/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   checker.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandres <roandres@student.42madrid.com>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/29                              #+#    #+#             */
/*   Updated: 2026/04/29                              ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static int    exec_instruction(char *line, t_stack_node **a, t_stack_node **b)
{
    if (!ft_strncmp(line, "sa\n", 3))
        sa(a, 1);
    else if (!ft_strncmp(line, "sb\n", 3))
        sb(b, 1);
    else if (!ft_strncmp(line, "ss\n", 3))
        ss(a, b, 1);
    else if (!ft_strncmp(line, "pa\n", 3))
        pa(a, b, 1);
    else if (!ft_strncmp(line, "pb\n", 3))
        pb(a, b, 1);
    else if (!ft_strncmp(line, "ra\n", 3))
        ra(a, 1);
    else if (!ft_strncmp(line, "rb\n", 3))
        rb(b, 1);
    else if (!ft_strncmp(line, "rr\n", 3))
        rr(a, b, 1);
    else if (!ft_strncmp(line, "rra\n", 4))
        rra(a, 1);
    else if (!ft_strncmp(line, "rrb\n", 4))
        rrb(b, 1);
    else if (!ft_strncmp(line, "rrr\n", 4))
        rrr(a, b, 1);
    else
        return (0);
    return (1);
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
    while ((line = get_next_line(0)))
    {
        if (!exec_instruction(line, &a, &b))
        {
            free(line);
            free_stack(a);
            free_stack(b);
            return (write(2, "Error\n", 6), 1);
        }
        free(line);
    }
    if (stack_sorted(a) && !b)
        write(1, "OK\n", 3);
    else
        write(1, "KO\n", 3);
    free_stack(a);
    free_stack(b);
    return (0);
}
