#include "ft_printf_bonus.h"

void	ft_putchar_fd_count(char c)
{
	write(1, &c, 1);
}
