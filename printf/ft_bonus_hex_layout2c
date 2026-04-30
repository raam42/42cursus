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

static int    get_hex_dlen(unsigned long nb, t_format *f)
{
    int    dlen;

    dlen = ulen_base(nb, 16);
    if (f->dot && f->precision == 0 && nb == 0)
        dlen = 0;
    return (dlen);
}

static int    print_hex_body(unsigned long nb, const char *base, int dlen, int zprec)
{
    int    count;

    count = 0;
    count += putnchar('0', zprec);
    if (dlen > 0)
        count += put_unsigned_base(nb, base, 16);
    return (count);
}

int    print_hex_layout(unsigned long nb, const char *base,
        const char *pre, int pre_len, t_format *f)
{
    int        dlen;
    int        zprec;
    int        pad;
    char    padc;
    int        count;

    dlen = get_hex_dlen(nb, f);
    zprec = get_zprec(f, dlen);
    padc = get_padc(f);
    pad = ft_max(0, f->width - pre_len - dlen - zprec);
    count = 0;
    if (!f->minus && padc == ' ')
        count += putnchar(' ', pad);
    if (pre_len)
        count += putnstr(pre, pre_len);
    if (!f->minus && padc == '0')
        count += putnchar('0', pad);
    count += print_hex_body(nb, base, dlen, zprec);
    if (f->minus)
        count += putnchar(' ', pad);
    return (count);
}
