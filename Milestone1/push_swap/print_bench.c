/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   print_bench.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandres <roandres@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/29 15:20:35 by roandres          #+#    #+#             */
/*   Updated: 2026/04/29 15:22:18 by roandres         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"
/* We only need to check if we already have the fd functions from libft to replace the write */
static void    put_2digits_fd(int n, int fd)
{
    char    c;

    c = '0' + (n / 10);
    write(fd, &c, 1);
    c = '0' + (n % 10);
    write(fd, &c, 1);
}

static void    print_disorder_pct(t_ctx *ctx)
{
    int    scaled;
    int    whole;
    int    dec;

    scaled = (int)(ctx->b.disorder * 10000.0f + 0.5f);
    whole = scaled / 100;
    dec = scaled % 100;
    ft_putstr_fd("[bench] disorder: ", 2);
    ft_putnbr_fd(whole, 2);
    write(2, ".", 1);
    put_2digits_fd(dec, 2);
    ft_putstr_fd("%\n", 2);
}

static void    print_strategy_line(t_ctx *ctx)
{
    ft_putstr_fd("[bench] strategy: ", 2);
    if (ctx->b.used_strategy == LINEAR)
        ft_putstr_fd("linear (O(n))\n", 2);
    else if (ctx->b.used_strategy == SIMPLE)
        ft_putstr_fd("simple (O(n^2))\n", 2);
    else if (ctx->b.used_strategy == MEDIUM)
        ft_putstr_fd("medium (O(n*sqrt(n)))\n", 2);
    else if (ctx->b.used_strategy == COMPLEX)
        ft_putstr_fd("complex (O(n*log(n)))\n", 2);
    else
        ft_putstr_fd("unresolved\n", 2);
}

static void    print_counts1(t_ctx *ctx)
{
    ft_putstr_fd("[bench] total_ops: ", 2);
    ft_putnbr_fd((int)ctx->b.total, 2);
    ft_putstr_fd("\n", 2);
    ft_putstr_fd("[bench] sa: ", 2);
    ft_putnbr_fd((int)ctx->b.sa, 2);
    ft_putstr_fd(" sb: ", 2);
    ft_putnbr_fd((int)ctx->b.sb, 2);
    ft_putstr_fd(" ss: ", 2);
    ft_putnbr_fd((int)ctx->b.ss, 2);
    ft_putstr_fd("\n", 2);
    ft_putstr_fd("[bench] pa: ", 2);
    ft_putnbr_fd((int)ctx->b.pa, 2);
    ft_putstr_fd(" pb: ", 2);
    ft_putnbr_fd((int)ctx->b.pb, 2);
    ft_putstr_fd("\n", 2);
}

static void    print_counts2(t_ctx *ctx)
{
    ft_putstr_fd("[bench] ra: ", 2);
    ft_putnbr_fd((int)ctx->b.ra, 2);
    ft_putstr_fd(" rb: ", 2);
    ft_putnbr_fd((int)ctx->b.rb, 2);
    ft_putstr_fd(" rr: ", 2);
    ft_putnbr_fd((int)ctx->b.rr, 2);
    ft_putstr_fd("\n", 2);
    ft_putstr_fd("[bench] rra: ", 2);
    ft_putnbr_fd((int)ctx->b.rra, 2);
    ft_putstr_fd(" rrb: ", 2);
    ft_putnbr_fd((int)ctx->b.rrb, 2);
    ft_putstr_fd(" rrr: ", 2);
    ft_putnbr_fd((int)ctx->b.rrr, 2);
    ft_putstr_fd("\n", 2);
}

void    print_bench(t_ctx *ctx)
{
    if (!ctx || !ctx->bench)
        return ;
    print_disorder_pct(ctx);
    print_strategy_line(ctx);
    print_counts1(ctx);
    print_counts2(ctx);
}
