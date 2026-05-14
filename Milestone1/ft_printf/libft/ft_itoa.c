/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_itoa.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: rodrigoa <rodrigoa@student.42madrid.c      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/23 13:41:33 by rodrigoa          #+#    #+#             */
/*   Updated: 2026/01/27 14:59:44 by rodrigoa         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"
#include <stdlib.h>

static size_t	ft_numlen(long n)
{
	size_t	i;

	i = (n <= 0);
	if (n <= 0)
		n *= -1;
	while (n > 0)
	{
		n /= 10;
		i++;
	}
	return (i);
}

static char	*ft_convert(char *str, long n, size_t len)
{
	str[len--] = '\0';
	if (n == 0)
		str[len] = '0';
	if (n < 0)
	{
		str[0] = '-';
		n *= -1;
	}
	while (n > 0)
	{
		str[len--] = (n % 10) + '0';
		n /= 10;
	}
	return (str);
}

char	*ft_itoa(int n)
{
	char	*str;
	size_t	len;

	len = ft_numlen(n);
	str = (char *)malloc((len + 1) * sizeof(char));
	if (!str)
		return (NULL);
	ft_convert(str, n, len);
	return (str);
}
