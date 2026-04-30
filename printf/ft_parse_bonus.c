#include "ft_printf_bonus.h"

static int    is_digit(char c)
{
    return (c >= '0' && c <= '9');
}

static int    is_flag(char c)
{
    return (c == '-' || c == '0' || c == '#'
        || c == '+' || c == ' ');
}

static int    is_specifier(char c)
{
    return (c == 'c' || c == 's' || c == 'p' || c == 'd' || c == 'i'
        || c == 'u' || c == 'x' || c == 'X' || c == '%');
}

static int    parse_number(const char *s, int i)
{
    int    n;

    n = 0;
    while (is_digit(s[i]))
    {
        n = n * 10 + (s[i] - '0');
        i++;
    }
    return (n);
}

void    init_format(t_format *fmt)
{
    fmt->minus = 0;
    fmt->zero = 0;
    fmt->width = 0;
    fmt->dot = 0;
    fmt->precision = 0;
    fmt->hash = 0;
    fmt->plus = 0;
    fmt->space = 0;
    fmt->specifier = 0;
}

static void    apply_flag(t_format *fmt, char c)
{
    if (c == '-')
        fmt->minus = 1;
    else if (c == '0')
        fmt->zero = 1;
    else if (c == '#')
        fmt->hash = 1;
    else if (c == '+')
        fmt->plus = 1;
    else if (c == ' ')
        fmt->space = 1;
}

/*
** parse_format:
** - s: full format string
** - i: index right AFTER '%' (caller passes i + 1)
** - fmt: filled format descriptor
**
** Returns:
** - index of the specifier character on success
** - -1 if no valid specifier is found
*/
int    parse_format(const char *s, int i, t_format *fmt)
{
    while (s[i] && is_flag(s[i]))
    {
        apply_flag(fmt, s[i]);
        i++;
    }
    if (is_digit(s[i]))
    {
        fmt->width = parse_number(s, i);
        while (is_digit(s[i]))
            i++;
    }
    if (s[i] == '.')
    {
        fmt->dot = 1;
        i++;
        if (is_digit(s[i]))
        {
            fmt->precision = parse_number(s, i);
            while (is_digit(s[i]))
                i++;
        }
        else
            fmt->precision = 0;
    }
    if (!s[i] || !is_specifier(s[i]))
        return (-1);
    fmt->specifier = s[i];
    if (fmt->plus)
        fmt->space = 0;
    if (fmt->minus)
        fmt->zero = 0;
    return (i);
}
