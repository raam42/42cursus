#ifndef FT_PRINTF_BONUS_H
# define FT_PRINTF_BONUS_H

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
** Bonus printing entry point
*/
int        handle_conversion_bonus(va_list args, t_format *fmt);

#endif
