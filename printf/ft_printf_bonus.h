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
int        ft_printf_bonus(const char *format, ...);

int    ft_max(int a, int b);
int    put_char_count(char c);
int    putnchar(char c, int n);
int    putnstr(const char *s, int n);
int    dec_len_unsigned(unsigned long n);
int    ulen_base(unsigned long n, int base);
int    put_dec_unsigned(unsigned long n);
int    put_unsigned_base(unsigned long n, const char *base, int b);

int    print_char_bonus(int c, t_format *f);
int    print_str_bonus(char *s, t_format *f);
int    print_int_bonus(int n, t_format *f);
int    print_uint_bonus(unsigned int n, t_format *f);
int    print_hex_bonus(unsigned int n, t_format *f, int upper);
int    print_ptr_bonus(void *p, t_format *f);

int    print_int_layout(unsigned long absn, char sign, int body, t_format *f);
int    print_uint_layout(unsigned long nb, int body, t_format *f, int zprec);
int    print_hex_layout(unsigned long nb, const char *base,
            const char *pre, int pre_len, t_format *f);
int    print_ptr_layout(unsigned long addr, t_format *f);
#endif
