#include "ft_printf.h"

int	ft_formats(va_list args, const char format)
{
	int	len;

	len = 0;
	if (format == 'c')
		len += ft_print_char(va_arg(args, int));
	else if (format == 's')
		len += ft_print_str(va_arg(args, char *));
	else if (format == 'p')
		len += ft_print_ptr(va_arg(args, unsigned long long));
	else if (format == 'd' || format == 'i')
		len += ft_print_nbr(va_arg(args, int));
	else if (format == 'u')
		len += ft_print_unsigned(va_arg(args, unsigned int));
	else if (format == 'x' || format == 'X')
		len += ft_print_hex(va_arg(args, unsigned int), format);
	else if (format == '%')
		len += ft_print_char('%');
	return (len);
}

int	ft_printf(const char *format, ...)
{
	int	i;
	int	print_len;
	va_list	args;

	if (!format)
		return (-1);
	i = 0;
	print_len = 0;
	va_start(args, format);
	while (format[i])
	{
		if (format[i] == '%')
		{
			print_len += ft_formats(args, format[i + 1]);
			i++;
		}
		else
			print_len += ft_print_char(format[i]);
		i++;
	}
	va_end(args);
	return (print_len);
}