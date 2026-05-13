#include "ft_printf_bonus.h"

int    ulen_base(unsigned long n, int base)
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

int    put_dec_unsigned(unsigned long n)
{
    int    count;

    count = 0;
    if (n >= 10)
        count += put_dec_unsigned(n / 10);
    count += put_char_count((char)('0' + (n % 10)));
    return (count);
}

int    put_unsigned_base(unsigned long n, const char *base, int b)
{
    int    count;

    count = 0;
    if (n >= (unsigned long)b)
        count += put_unsigned_base(n / (unsigned long)b, base, b);
    count += put_char_count(base[n % (unsigned long)b]);
    return (count);
}
