#include "ft_printf.h"

static int    print_ptr_recursive(unsigned long n)
{
    int    count;

    count = 0;
    if (n >= 16)
        count += print_ptr_recursive(n / 16);
    ft_putchar("0123456789abcdef"[n % 16]);
    return (count + 1);
}

int    ft_print_ptr(void *p)
{
    unsigned long    addr;
    int                count;

    if (!p)
    {
        ft_putstr("0x0");
        return (3);
    }
    addr = (unsigned long)p;
    count = 0;
    ft_putstr("0x");
    count += 2;
    count += print_ptr_recursive(addr);
    return (count);
}
