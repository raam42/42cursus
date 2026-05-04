#include "ft_printf_bonus.h"

static void    get_hex_prefix(unsigned long nb, t_format *f, int upper,
                            const char **pre, int *pre_len)
{
    *pre = NULL;
    *pre_len = 0;
    if (!f->hash || nb == 0)
        return ;
    if (upper)
    {
        *pre = "0X";
        *pre_len = 2;
    }
    else
    {
        *pre = "0x";
        *pre_len = 2;
    }
}

int    print_hex_bonus(unsigned int n, t_format *f, int upper)
{
    const char    *base;
    unsigned long    nb;
    const char    *pre;
    int            pre_len;

    base = "0123456789abcdef";
    if (upper)
        base = "0123456789ABCDEF";
    nb = (unsigned long)n;
    get_hex_prefix(nb, f, upper, &pre, &pre_len);
    return (print_hex_layout(nb, base, pre, pre_len, f));
}

int    print_ptr_bonus(void *p, t_format *f)
{
    return (print_ptr_layout((unsigned long)p, f));
}
