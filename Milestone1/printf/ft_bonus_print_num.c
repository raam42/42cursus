#include "ft_printf_bonus.h"

static char    get_int_sign(long nb, t_format *f)
{
    if (nb < 0)
        return ('-');
    if (f->plus)
        return ('+');
    if (f->space)
        return (' ');
    return (0);
}

int    print_int_bonus(int n, t_format *f)
{
    long            nb;
    unsigned long    absn;
    char            sign;
    int                dlen;
    int                zprec;

    nb = (long)n;
    sign = get_int_sign(nb, f);
    if (nb < 0)
        absn = (unsigned long)(-nb);
    else
        absn = (unsigned long)nb;
    dlen = dec_len_unsigned(absn);
    if (f->dot && f->precision == 0 && absn == 0)
        dlen = 0;
    zprec = 0;
    if (f->dot)
        zprec = ft_max(0, f->precision - dlen);
    return (print_int_layout(absn, sign, dlen + zprec, f));
}

int    print_uint_bonus(unsigned int n, t_format *f)
{
    unsigned long    nb;
    int                dlen;
    int                zprec;

    nb = (unsigned long)n;
    dlen = dec_len_unsigned(nb);
    if (f->dot && f->precision == 0 && nb == 0)
        dlen = 0;
    zprec = 0;
    if (f->dot)
        zprec = ft_max(0, f->precision - dlen);
    return (print_uint_layout(nb, dlen + zprec, f, zprec));
}
