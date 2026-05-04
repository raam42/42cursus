#include "push_swap.h"

static void	rotate_to_sorted(t_stack_node **a, int size)
{
	int	i;
	t_stack_node *cur;

	cur = *a;
	i = 0;
	while (cur && cur->next)
	{
		if (cur->value > cur->next->value)
			break ;
		cur = cur->next;
		i++;
	}
	if (i + 1 <= size / 2)
	{
		i++;
		while (i--)
			ra(a, 0);
	}
	else
	{
		i = size - i - 1;
		while (i--)
			rra(a, 0);
	}
}

static int	is_rotated_sorted(t_stack_node *a)
{
	int	breaks;

	breaks = 0;
	while (a && a->next)
	{
		if (a->value > a->next->value)
			breaks++;
		a = a->next;
	}
	return (breaks == 1);
}

static void	fix_pass(t_stack_node **a, int size)
{
	int	i;

	i = 0;
	while (i < size)
	{
		if ((*a)->next && (*a)->value > (*a)->next->value)
			sa(a, 0);
		ra(a, 0);
		i++;
	}
}

int	linear_sort(t_stack_node **a)
{
	int	size;
	int	passes;
	int	max_passes;

	if (!a || !*a || stack_sorted(*a))
		return (1);

	size = len_stack(*a);
	max_passes = 3;
	passes = 0;
	while (passes < max_passes)
	{
		fix_pass(a, size);
		if (stack_sorted(*a))
			return (1);
		if (is_rotated_sorted(*a))
		{
			rotate_to_sorted(a, size);
			return (stack_sorted(*a));
		}
		passes++;
	}
	return (0);
}
