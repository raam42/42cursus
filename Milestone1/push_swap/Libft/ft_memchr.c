/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memchr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: rodri <rodri@student.42.fr>                +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/19 19:01:38 by roandres          #+#    #+#             */
/*   Updated: 2026/01/29 06:11:07 by rodri            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_memchr(const void *s, int c, size_t n)
{
	size_t			i;
	unsigned char	*p;
	unsigned char	uc;

	i = 0;
	p = (unsigned char *)s;
	uc = (unsigned char)c;
	while (i < n)
	{
		if (p[i] == uc)
			return (p + i);
		i++;
	}
	return (NULL);
}
