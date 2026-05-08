#include "ft_printf_bonus.h"

int    print_char_bonus(int c, t_format *f)
{
    int    pad;
    int    count;

    pad = 0;
    if (f->width > 1)
        pad = f->width - 1;
    count = 0;
    if (!f->minus)
        count += putnchar(' ', pad);
    count += put_char_count((char)c);
    if (f->minus)
        count += putnchar(' ', pad);
    return (count);
}

int    print_str_bonus(char *s, t_format *f)
{
    int    len;
    int    out_len;
    int    pad;
    int    count;

    if (!s)
        s = "(null)";
    len = (int)ft_strlen(s);
    out_len = len;
    if (f->dot && f->precision < out_len)
        out_len = f->precision;
    pad = 0;
    if (f->width > out_len)
        pad = f->width - out_len;
    count = 0;
    if (!f->minus)
        count += putnchar(' ', pad);
    count += putnstr(s, out_len);
    if (f->minus)
        count += putnchar(' ', pad);
    return (count);
}
