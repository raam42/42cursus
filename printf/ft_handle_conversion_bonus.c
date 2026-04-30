#include "ft_printf_bonus.h"

static int    ft_max(int a, int b)
{
    if (a > b)
        return (a);
    return (b);
}

static int    putnchar(char c, int n)
{
    int    count;

    count = 0;
    while (n-- > 0)
    {
        ft_putchar(c);
        count++;
    }
    return (count);
}

static int    putnstr(const char *s, int n)
{
    int    count;

    count = 0;
    while (s && *s && n-- > 0)
    {
        ft_putchar(*s++);
        count++;
    }
    return (count);
}

static int    ulen_base(unsigned long n, int base)
{
    int    len;

    len = 1;
    while (n >= (unsigned long)base)
    {
        n /= (unsigned long)base;
        len++;
    }
    return (len);
}

static int    put_unsigned_base(unsigned long n, const char *base)
{
    int    count;

    count = 0;
    if (n >= 16)
        count += put_unsigned_base(n / 16, base);
    ft_putchar(base[n % 16]);
    return (count + 1);
}

static int    put_unsigned_base_b(unsigned long n, const char *base, int b)
{
    int    count;

    count = 0;
    if (n >= (unsigned long)b)
        count += put_unsigned_base_b(n / (unsigned long)b, base, b);
    ft_putchar(base[n % (unsigned long)b]);
    return (count + 1);
}

/* ----------------------------- %c and %% ----------------------------- */

static int    print_char_bonus(int c, t_format *f)
{
    int    pad;
    int    count;

    pad = 0;
    count = 0;
    if (f->width > 1)
        pad = f->width - 1;
    if (!f->minus)
        count += putnchar(' ', pad);
    ft_putchar((char)c);
    count++;
    if (f->minus)
        count += putnchar(' ', pad);
    return (count);
}

/* ------------------------------ %s ----------------------------------- */

static int    print_str_bonus(char *s, t_format *f)
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

/* -------------------------- numbers helpers --------------------------- */

static int    print_sign_prefix(char sign, const char *pre, int pre_len)
{
    int    count;

    count = 0;
    if (sign)
    {
        ft_putchar(sign);
        count++;
    }
    if (pre && pre_len > 0)
        count += putnstr(pre, pre_len);
    return (count);
}

static int    print_dec_digits(long n)
{
    int    count;

    count = 0;
    if (n >= 10)
        count += print_dec_digits(n / 10);
    ft_putchar((char)('0' + (n % 10)));
    return (count + 1);
}

static int    dec_len_unsigned(unsigned long n)
{
    int    len;

    len = 1;
    while (n >= 10)
    {
        n /= 10;
        len++;
    }
    return (len);
}

/* ------------------------------ %d/%i -------------------------------- */

static int    print_int_bonus(int n, t_format *f)
{
    long    nb;
    char    sign;
    int        dlen;
    int        zprec;
    int        pad;
    char    padc;
    int        count;

    nb = (long)n;
    sign = 0;
    if (nb < 0)
        sign = '-';
    else if (f->plus)
        sign = '+';
    else if (f->space)
        sign = ' ';
    if (nb < 0)
        nb = -nb;
    dlen = dec_len_unsigned((unsigned long)nb);
    if (f->dot && f->precision == 0 && nb == 0)
        dlen = 0;
    zprec = 0;
    if (f->dot)
        zprec = ft_max(0, f->precision - dlen);
    padc = ' ';
    if (f->zero && !f->minus && !f->dot)
        padc = '0';
    pad = 0;
    if (f->width > (dlen + zprec + (sign != 0)))
        pad = f->width - (dlen + zprec + (sign != 0));
    count = 0;
    if (!f->minus && padc == ' ')
        count += putnchar(' ', pad);
    if (padc == '0')
    {
        if (sign)
            count += print_sign_prefix(sign, NULL, 0);
        count += putnchar('0', pad);
    }
    else
        count += print_sign_prefix(sign, NULL, 0);
    count += putnchar('0', zprec);
    if (dlen > 0)
        count += print_dec_digits(nb);
    if (f->minus)
        count += putnchar(' ', pad);
    return (count);
}

/* ------------------------------ %u ----------------------------------- */

static int    print_uint_bonus(unsigned int n, t_format *f)
{
    unsigned long    nb;
    int                dlen;
    int                zprec;
    int                pad;
    char            padc;
    int                count;

    nb = (unsigned long)n;
    dlen = dec_len_unsigned(nb);
    if (f->dot && f->precision == 0 && nb == 0)
        dlen = 0;
    zprec = 0;
    if (f->dot)
        zprec = ft_max(0, f->precision - dlen);
    padc = ' ';
    if (f->zero && !f->minus && !f->dot)
        padc = '0';
    pad = 0;
    if (f->width > (dlen + zprec))
        pad = f->width - (dlen + zprec);
    count = 0;
    if (!f->minus && padc == ' ')
        count += putnchar(' ', pad);
    if (padc == '0')
        count += putnchar('0', pad);
    count += putnchar('0', zprec);
    if (dlen > 0)
        count += print_dec_digits((long)nb);
    if (f->minus)
        count += putnchar(' ', pad);
    return (count);
}

/* --------------------------- %x / %X --------------------------------- */

static int    print_hex_bonus(unsigned int n, t_format *f, int upper)
{
    const char        *base;
    unsigned long    nb;
    const char        *pre;
    int                pre_len;
    int                dlen;
    int                zprec;
    int                pad;
    char            padc;
    int                count;

    base = "0123456789abcdef";
    if (upper)
        base = "0123456789ABCDEF";
    nb = (unsigned long)n;
    pre = NULL;
    pre_len = 0;
    if (f->hash && nb != 0 && upper)
        (pre = "0X", pre_len = 2);
    else if (f->hash && nb != 0 && !upper)
        (pre = "0x", pre_len = 2);
    dlen = ulen_base(nb, 16);
    if (f->dot && f->precision == 0 && nb == 0)
        dlen = 0;
    zprec = 0;
    if (f->dot)
        zprec = ft_max(0, f->precision - dlen);
    padc = ' ';
    if (f->zero && !f->minus && !f->dot)
        padc = '0';
    pad = 0;
    if (f->width > (pre_len + dlen + zprec))
        pad = f->width - (pre_len + dlen + zprec);
    count = 0;
    if (!f->minus && padc == ' ')
        count += putnchar(' ', pad);
    count += print_sign_prefix(0, pre, pre_len);
    if (padc == '0')
        count += putnchar('0', pad);
    count += putnchar('0', zprec);
    if (dlen > 0)
        count += put_unsigned_base_b(nb, base, 16);
    if (f->minus)
        count += putnchar(' ', pad);
    return (count);
}

/* ------------------------------ %p ----------------------------------- */

static int    print_ptr_bonus(void *p, t_format *f)
{
    unsigned long    addr;
    int                dlen;
    int                zprec;
    int                pad;
    char            padc;
    int                count;

    addr = (unsigned long)p;
    dlen = ulen_base(addr, 16);
    if (f->dot && f->precision == 0 && addr == 0)
        dlen = 0;
    zprec = 0;
    if (f->dot)
        zprec = ft_max(0, f->precision - dlen);
    padc = ' ';
    if (f->zero && !f->minus && !f->dot)
        padc = '0';
    pad = 0;
    if (f->width > (2 + dlen + zprec))
        pad = f->width - (2 + dlen + zprec);
    count = 0;
    if (!f->minus && padc == ' ')
        count += putnchar(' ', pad);
    count += putnstr("0x", 2);
    if (padc == '0')
        count += putnchar('0', pad);
    count += putnchar('0', zprec);
    if (dlen > 0)
        count += put_unsigned_base_b(addr, "0123456789abcdef", 16);
    if (f->minus)
        count += putnchar(' ', pad);
    return (count);
}

/* ---------------------- BONUS DISPATCH ENTRY POINT --------------------- */

int    handle_conversion_bonus(va_list args, t_format *fmt)
{
    if (fmt->specifier == 'c')
        return (print_char_bonus(va_arg(args, int), fmt));
    if (fmt->specifier == 's')
        return (print_str_bonus(va_arg(args, char *), fmt));
    if (fmt->specifier == 'p')
        return (print_ptr_bonus(va_arg(args, void *), fmt));
    if (fmt->specifier == 'd' || fmt->specifier == 'i')
        return (print_int_bonus(va_arg(args, int), fmt));
    if (fmt->specifier == 'u')
        return (print_uint_bonus(va_arg(args, unsigned int), fmt));
    if (fmt->specifier == 'x')
        return (print_hex_bonus(va_arg(args, unsigned int), fmt, 0));
    if (fmt->specifier == 'X')
        return (print_hex_bonus(va_arg(args, unsigned int), fmt, 1));
    if (fmt->specifier == '%')
        return (print_char_bonus('%', fmt));
    return (0);
}
