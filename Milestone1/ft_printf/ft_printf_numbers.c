/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf_numbers.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: rodrigoa <rodrigoa@student.42madrid.c      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/14 03:07:54 by rodrigoa          #+#    #+#             */
/*   Updated: 2026/05/14 03:36:44 by rodrigoa         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "ft_printf.h"

int	ft_print_nbr(int n)
{
	int		len;
	long	num;

	len = 0;
	num = n;
	if (num < 0)
	{
		len += ft_print_char('-');
		num *= -1;
	}
	if (num >= 10)
		len += ft_print_nbr(num / 10);
	len += ft_print_char((num % 10) + 48);
	return (len);
}

int	ft_print_unsigned(unsigned int n)
{
	int	len;

	len = 0;
	if (n >= 10)
		len += ft_print_unsigned(n / 10);
	len += ft_print_char((n % 10) + 48);
	return (len);
}

int	ft_print_hex(unsigned int n, char format)
{
	int		len;
	char	*base;

	len = 0;
	if (format == 'x')
		base = "0123456789abcdef";
	else
		base = "0123456789ABCDEF";
	if (n >= 16)
		len += ft_print_hex(n / 16, format);
	len += ft_print_char(base[n % 16]);
	return (len);
}
