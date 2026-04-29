#ifndef FT_PRINTF_H
# define FT_PRINTF_H

# include <stdarg.h>
# include <unistd.h>
# include <stdlib.h>

/*
** libft output helpers (already implemented in libft)
*/
void    ft_putchar(char c);
void    ft_putstr(char *s);
int        ft_strlen(const char *s);

/*
** ft_printf main function
*/
int        ft_printf(const char *format, ...);

/*
** Conversion handlers
*/
int        ft_print_char(int c);
int        ft_print_str(char *s);
int        ft_print_ptr(void *p);
int        ft_print_int(int n);
int        ft_print_uint(unsigned int n);
int        ft_print_hex(unsigned int n, int uppercase);

#endif
