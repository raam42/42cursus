#include "ft_printf_bonus.h"

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
