#include "ft_printf_bonus.h"

int	ft_printf(const char *format, ...)
{
	va_list	args;
	t_format	fmt;
	int	total;
	int	i;
	int	j;

	if (!format)
		return (-1);
	va_start(args, format);
	total = 0;
	i = 0;
	while (format[i])
	{
		if (format[i] == '%')
		{
			if (!format[i + 1])
				return (va_end(args), -1);
			init_format(&fmt);
			j = parse_format(format, i + 1, &fmt);
			if (j < 0)
			{
				j = put_char_count('%');
				if (j < 0)
					return (va_end(args), -1);
				total += j;
				i++;
				continue ;
			}
			i = j + 1;
			j = handle_conversion_bonus(args, &fmt);
			if (j < 0)
				return (va_end(args), -1);
			total += j;
		}
		else
		{
			j = put_char_count(format[i]);
			if (j < 0)
				return (va_end(args), -1);
			total += j;
			i++;
		}
	}
	va_end(args);
	return (total);
}
