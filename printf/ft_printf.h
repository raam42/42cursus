#ifndef FT_PRINTF_BONUS_H
# define FT_PRINTF_BONUS_H

# include <stdarg.h>
# include "ft_printf.h"

/*
** Bonus format descriptor
*/
typedef struct s_format
{
    int        minus;
    int        zero;
    int        width;
    int        dot;
    int        precision;
    int        hash;
    int        plus;
    int        space;
    char    specifier;
}    t_format;

/*
** Bonus parsing
*/
void    init_format(t_format *fmt);
int        parse_format(const char *s, int i, t_format *fmt);

/*
** Bonus entry points
*/
int        ft_printf_bonus(const char *format, ...);
int        handle_conversion_bonus(va_list args, t_format *fmt);

/*
** Bonus layout (shared)
*/
int        print_hex_layout(unsigned long nb, const char *base,
            const char *pre, int pre_len, t_format *f);
int        print_ptr_layout(unsigned long addr, t_format *f);

#endif
