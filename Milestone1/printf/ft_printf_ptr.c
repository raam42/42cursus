#include "ft_printf.h"

static int  ft_ptr_len(unsigned long long n)
{
    int len;

    len = 0;
    if (n >= 16)
        len += ft_ptr_len(n / 16);
    len += ft_print_char("0123456789abcdef"[n % 16]);
    return (len);
}

int ft_print_ptr(unsigned long long ptr)
{
    int len;

    len = 0;
    if (ptr == 0)
    {
        len += ft_print_str("(nil)");
        return (len);
    }
    len += ft_print_str("0x");
    len += ft_ptr_len(ptr);
    return (len);
}