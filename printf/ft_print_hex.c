#include "ft_printf.h"

static int    print_hex_recursive(unsigned int n, char *base)
{
    int    count;

    count = 0;
    if (n >= 16)
        count += print_hex_recursive(n / 16, base);
    ft_putchar(base[n % 16]);
    return (count + 1);
}

int    ft_print_hex(unsigned int n, int uppercase)
{
    char    *base;

    if (uppercase)
        base = "0123456789ABCDEF";
    else
        base = "0123456789abcdef";
    return (print_hex_recursive(n, base));
}
