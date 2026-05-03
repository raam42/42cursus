#include "ft_printf.h"

void	ft_putchar(char c)
{
	write(1, &c, 1);
}

int	ft_print_char(char c)
{
	write(1, &c, 1);
	return (1);
}
