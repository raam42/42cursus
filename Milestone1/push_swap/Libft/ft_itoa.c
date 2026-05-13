/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_itoa.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: rodri <rodri@student.42.fr>                +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/29 06:08:00 by rodri             #+#    #+#             */
/*   Updated: 2026/02/01 19:06:36 by rodri            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static int	count_n(long int n)
{
	int	count;

	count = 0;
	if (n <= 0)
		count++;
	while (n)
	{
		n = n / 10;
		count++;
	}
	return (count);
}

char	*ft_itoa(int n)
{
	char	*str;
	int		nlen;
	size_t	i;

	nlen = count_n(n);
	i = nlen;
	if (n == -2147483648)
		return (ft_strdup("-2147483648"));
	str = malloc((nlen + 1) * sizeof(char));
	if (!str)
		return (NULL);
	if (n < 0)
	{
		n = -n;
		str[0] = '-';
	}
	str[nlen] = '\0';
	while (i > 0 && str[i - 1] != '-')
	{
		i--;
		str[i] = (n % 10) + '0';
		n /= 10;
	}
	return (str);
}
