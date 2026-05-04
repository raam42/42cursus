#include "ft_printf_bonus.h"

int	ft_printf_bonus(const char *format, ...)
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
			init_format(&fmt);
			j = parse_format(format, i + 1, &fmt);
			if (j < 0)
			{
				ft_putchar_fd('%', 1);
				total++;
				i++;
				continue ;
			}
			total += handle_conversion_bonus(args, &fmt);
			i = j + 1;
		}
		else
		{
			ft_putchar_fd(format[i], 1);
			total++;
			i++;
		}
	}
	va_end(args);
	return (total);
}
