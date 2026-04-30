#include "ft_printf.h"

static int    handle_conversion(char specifier, va_list args)
{
    if (specifier == 'c')
        return (ft_print_char(va_arg(args, int)));
    if (specifier == 's')
        return (ft_print_str(va_arg(args, char *)));
    if (specifier == 'p')
        return (ft_print_ptr(va_arg(args, void *)));
    if (specifier == 'd' || specifier == 'i')
        return (ft_print_int(va_arg(args, int)));
    if (specifier == 'u')
        return (ft_print_uint(va_arg(args, unsigned int)));
    if (specifier == 'x')
        return (ft_print_hex(va_arg(args, unsigned int), 0));
    if (specifier == 'X')
        return (ft_print_hex(va_arg(args, unsigned int), 1));
    if (specifier == '%')
        return (ft_print_char('%'));
    return (0);
}

int    ft_printf(const char *format, ...)
{
    va_list    args;
    int        total;
    int        i;

    if (!format)
        return (-1);
    va_start(args, format);
    total = 0;
    i = 0;
    while (format[i])
    {
        if (format[i] == '%' && format[i + 1])
        {
            total += handle_conversion(format[i + 1], args);
            i += 2;
        }
        else
        {
            ft_putchar(format[i]);
            total++;
            i++;
        }
    }
    va_end(args);
    return (total);
}
