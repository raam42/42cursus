#include "ft_printf_bonus.h"

static char    get_padc(t_format *f)
{
    if (f->zero && !f->minus && !f->dot)
        return ('0');
    return (' ');
}

static int    get_zprec(t_format *f, int dlen)
{
    int    zprec;

    zprec = 0;
    if (f->dot)
        zprec = ft_max(0, f->precision - dlen);
    return (zprec);
}

static int    get_ptr_dlen(unsigned long addr)
{
    int    dlen;

    dlen = 1;
    if (addr != 0)
        dlen = ulen_base(addr, 16);
    return (dlen);
}

static int    print_ptr_body(unsigned long addr, int zprec)
{
    int    count;

    count = 0;
    count += putnchar('0', zprec);
    if (addr == 0)
        count += put_char_count('0');
    else
        count += put_unsigned_base(addr, "0123456789abcdef", 16);
    return (count);
}

int    print_ptr_layout(unsigned long addr, t_format *f)
{
    int        dlen;
    int        zprec;
    int        pad;
    char    padc;
    int        count;

    dlen = get_ptr_dlen(addr);
    zprec = get_zprec(f, dlen);
    padc = get_padc(f);
    pad = ft_max(0, f->width - 2 - dlen - zprec);
    count = 0;
    if (!f->minus && padc == ' ')
        count += putnchar(' ', pad);
    count += putnstr("0x", 2);
    if (!f->minus && padc == '0')
        count += putnchar('0', pad);
    count += print_ptr_body(addr, zprec);
    if (f->minus)
        count += putnchar(' ', pad);
    return (count);
}
