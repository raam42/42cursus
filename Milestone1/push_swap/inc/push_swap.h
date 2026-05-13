/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandres <roandres@student.42madrid.com    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/17 18:19:28 by roandres          #+#    #+#             */
/*   Updated: 2026/05/02 17:45:53 by roandres         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef PUSH_SWAP_H
# define PUSH_SWAP_H

# include "../Libft/libft.h"
# include <stdlib.h>
# include <limits.h>
# include <unistd.h>

typedef enum e_strategy
{
	ADAPTIVE,
	SIMPLE,
	MEDIUM,
	COMPLEX
}	t_strategy;

typedef struct s_stack_node
{
	int					value; // real value (ej: -42, 100, 3)
	int					index; // final position that it should end (0 a N-1)
	struct s_stack_node	*next;
	struct s_stack_node	*prev;
	struct s_ctx		*ctx;
}	t_stack_node;

typedef struct s_bench
{
	long	sa;
	long	sb;
	long	ss;
	long	pa;
	long	pb;
	long	ra;
	long	rb;
	long	rr;
	long	rra;
	long	rrb;
	long	rrr;
	long	total;
	float	disorder;
	int		used_complexity;
	int		used_strategy;
}	t_bench;

typedef struct s_ctx
{
	t_strategy	strategy;
	int			bench;
	int			start_idx;
	t_bench		b;
}	t_ctx;

//PRINT BENCH
void			print_bench(t_ctx *ctx);

//FLAGS
int				parse_flags(char **argv, t_ctx *ctx);
int				init_ctx(int argc, char **argv, t_ctx *ctx);

//STRATEGY
void			run_strategy(t_stack_node **a, t_stack_node **b, t_ctx *ctx);

//PARSER
t_stack_node	*parse_and_fill_stack(int argc, char **argv, int start_idx,
					t_ctx *ctx);
int				is_valid_number(const char *str);
int				check_duplicate(t_stack_node *stack, int num);
void			add_to_stack(t_stack_node **stack, int num, t_ctx *ctx);

//UTILS
void			free_split(char **split);
void			free_stack(t_stack_node *stack);
int				ft_safe_atoi(const char *str, int *out);
t_stack_node	*last_node(t_stack_node *stack);
void			ft_putstr(char *str);
int				len_stack(t_stack_node *stack);
int				stack_sorted(t_stack_node *stack);

//MOVES
void			pa(t_stack_node **stack_a, t_stack_node **stack_b, int testing);
void			pb(t_stack_node **stack_a, t_stack_node **stack_b, int testing);
void			ra(t_stack_node **stack_a, int testing);
void			rb(t_stack_node **stack_b, int testing);
void			rr(t_stack_node **stack_a, t_stack_node **stack_b, int testing);
void			rra(t_stack_node **stack_a, int testing);
void			rrb(t_stack_node **stack_b, int testing);
void			rrr(t_stack_node **stack_a, t_stack_node **stack_b,
					int testing);
void			sa(t_stack_node **stack_a, int testing);
void			sb(t_stack_node **stack_b, int testing);
void			ss(t_stack_node **stack_a, t_stack_node **stack_b, int testing);

//ALGORITHMS
void			simple_sort(t_stack_node **a, t_stack_node **b);
void			medium_sort(t_stack_node **a, t_stack_node **b);
void			complex_sort(t_stack_node **a, t_stack_node **b);

void			set_node_index(t_stack_node *stack);
float			compute_disorder(t_stack_node *stack);

#endif
