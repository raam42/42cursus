#include "ft_printf.h"

static int    print_number(long n)
{
    int    count;

    count = 0;
    if (n >= 10)
        count += print_number(n / 10);
    ft_putchar((char)('0' + (n % 10)));
    return (count + 1);
}

int    ft_print_int(int n)
{
    long    nb;
    int        count;

    nb = n;
    count = 0;
    if (nb < 0)
    {
        ft_putchar('-');
        count++;
        nb = -nb;
    }
    count += print_number(nb);
    return (count);
}
