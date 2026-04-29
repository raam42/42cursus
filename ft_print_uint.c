#include "ft_printf.h"

static int    print_unsigned(unsigned int n)
{
    int    count;

    count = 0;
    if (n >= 10)
        count += print_unsigned(n / 10);
    ft_putchar((char)('0' + (n % 10)));
    return (count + 1);
}

int    ft_print_uint(unsigned int n)
{
    return (print_unsigned(n));
}
