#ifndef FT_PRINTF_H
# define FT_PRINTF_H

# include <unistd.h>
# include <stdarg.h>
# include "libft/libft.h"

int	ft_printf(const char *format, ...);

int ft_formats(va_list args, const char format);
int ft_print_char(int c);
int ft_print_str(char *str);
int ft_print_ptr(unsigned long long ptr);
int ft_print_nbr(int n);
int ft_print_unsigned(unsigned int n);
int ft_print_hex(unsigned int n, char format);

#endif
