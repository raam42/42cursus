/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcpy.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandres <roandres@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/12 20:22:53 by roandres          #+#    #+#             */
/*   Updated: 2026/01/29 21:21:27 by roandres         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

size_t	ft_strlcpy(char *dst, const char *src, size_t size)
{
	size_t	i;

	i = 0;
	if (!size)
		return (ft_strlen((char *)src));
	if (size > 0)
	{
		while (i < (size - 1) && src[i] != '\0')
		{
			dst [i] = src[i];
			i++;
		}
	}
	dst[i] = '\0';
	return (ft_strlen((char *)src));
}
