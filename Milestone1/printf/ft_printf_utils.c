#include "ft_printf.h"

int ft_print_char(int c)
{
    ft_putchar_fd(c, 1);
    return (1);
}

int ft_print_str(char *str)
{
    if (!str)
    {
        ft_putstr_fd("(null)", 1);
        return (6);
    }
    ft_putstr_fd(str, 1);
    return (ft_strlen(str));
}
