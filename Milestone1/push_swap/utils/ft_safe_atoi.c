/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_safe_atoi.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandres <roandres@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/23 14:53:04 by roandres          #+#    #+#             */
/*   Updated: 2026/05/05 13:29:27 by roandres         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

int	ft_safe_atoi(const char *str, int *out)
{
	int		i;
	long	nb;
	int		sign;

	i = 0;
	nb = 0;
	sign = 1;
	while (str[i] == 32 || (str[i] >= 9 && str[i] <= 13))
		i++;
	if (str[i] == 45 || str[i] == 43)
		if (str[i++] == 45)
			sign = -sign;
	while (str[i] >= 48 && str[i] <= 57)
	{
		nb = nb * 10 + (str[i++] - '0');
		if ((nb * sign) > INT_MAX || (nb * sign) < INT_MIN)
			return (0);
	}
	*out = (int)(nb * sign);
	return (1);
}
