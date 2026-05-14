/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_atoi.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: rodrigoa <rodrigoa@student.42madrid.c      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/16 13:06:55 by rodrigoa          #+#    #+#             */
/*   Updated: 2026/01/27 15:01:56 by rodrigoa         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

int	ft_atoi(const char *str)
{
	int	final;
	int	sign;
	int	index;

	final = 0;
	sign = 1;
	index = 0;
	while ((str[index] >= 9 && str[index] <= 13) || str[index] == 32)
		index++;
	if (str[index] == 45 || str[index] == 43)
	{
		if (str[index] == 45)
			sign = -1;
		index++;
	}
	while (str[index] >= 48 && str[index] <= 57)
	{
		final = final * 10 + str[index] - 48;
		index++;
	}
	return (final * sign);
}
