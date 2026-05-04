#include "ft_printf_bonus.h"

int	ft_max(int a, int b)
{
	if (a > b)
		return (a);
	return (b);
}

int	put_char_count(char c)
{
	ft_putchar_fd(c, 1);
	return (1);
}

int	putnchar(char c, int n)
{
	int	count;

	count = 0;
	while (n-- > 0)
		count += put_char_count(c);
	return (count);
}

int	putnstr(const char *s, int n)
{
	int	count;

	count = 0;
	while (s && *s && n-- > 0)
		count += put_char_count(*s++);
	return (count);
}

int	dec_len_unsigned(unsigned long n)
{
	int	len;

	len = 1;
	while (n >= 10)
	{
		n /= 10;
		len++;
	}
	return (len);
}
