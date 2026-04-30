#include "ft_printf_bonus.h"

int    print_hex_layout(unsigned long nb, const char *base,
                        const char *pre, int pre_len, t_format *f)
{
    int        dlen;
    int        zprec;
    int        pad;
    char    padc;
    int        count;

    dlen = ulen_base(nb, 16);
    if (f->dot && f->precision == 0 && nb == 0)
        dlen = 0;
    zprec = 0;
    if (f->dot)
        zprec = ft_max(0, f->precision - dlen);
    padc = ' ';
    if (f->zero && !f->minus && !f->dot)
        padc = '0';
    pad = ft_max(0, f->width - pre_len - dlen - zprec);
    count = 0;
    if (!f->minus && padc == ' ')
        count += putnchar(' ', pad);
    if (pre_len)
        count += putnstr(pre, pre_len);
    if (!f->minus && padc == '0')
        count += putnchar('0', pad);
    count += putnchar('0', zprec);
    if (dlen > 0)
        count += put_unsigned_base(nb, base, 16);
    if (f->minus)
        count += putnchar(' ', pad);
    return (count);
}

int    print_ptr_layout(unsigned long addr, t_format *f)
{
    int    dlen;
    int    zprec;
    int    pad;
    char    padc;
    int    count;

    dlen = 1;
    if (addr != 0)
        dlen = ulen_base(addr, 16);
    zprec = 0;
    if (f->dot)
        zprec = ft_max(0, f->precision - dlen);
    padc = ' ';
    if (f->zero && !f->minus && !f->dot)
        padc = '0';
    pad = ft_max(0, f->width - 2 - dlen - zprec);
    count = 0;
    if (!f->minus && padc == ' ')
        count += putnchar(' ', pad);
    count += putnstr("0x", 2);
    if (!f->minus && padc == '0')
        count += putnchar('0', pad);
    count += putnchar('0', zprec);
    if (addr == 0)
        count += put_char_count('0');
    else
        count += put_unsigned_base(addr, "0123456789abcdef", 16);
    if (f->minus)
        count += putnchar(' ', pad);
    return (count);
}
