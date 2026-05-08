#include "ft_printf_bonus.h"

int    print_int_layout(unsigned long absn, char sign, int body, t_format *f)
{
    int        pad;
    char    padc;
    int        count;

    padc = ' ';
    if (f->zero && !f->minus && !f->dot)
        padc = '0';
    pad = ft_max(0, f->width - body - (sign != 0));
    count = 0;
    if (!f->minus && padc == ' ')
        count += putnchar(' ', pad);
    if (sign)
        count += put_char_count(sign);
    if (!f->minus && padc == '0')
        count += putnchar('0', pad);
    count += putnchar('0', body - dec_len_unsigned(absn));
    if (body > 0 && !(f->dot && f->precision == 0 && absn == 0))
        count += put_dec_unsigned(absn);
    if (f->minus)
        count += putnchar(' ', pad);
    return (count);
}

int    print_uint_layout(unsigned long nb, int body, t_format *f, int zprec)
{
    int        pad;
    char    padc;
    int        count;

    padc = ' ';
    if (f->zero && !f->minus && !f->dot)
        padc = '0';
    pad = ft_max(0, f->width - body);
    count = 0;
    if (!f->minus && padc == ' ')
        count += putnchar(' ', pad);
    if (!f->minus && padc == '0')
        count += putnchar('0', pad);
    count += putnchar('0', zprec);
    if (body > 0 && !(f->dot && f->precision == 0 && nb == 0))
        count += put_dec_unsigned(nb);
    if (f->minus)
        count += putnchar(' ', pad);
    return (count);
}
