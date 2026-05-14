/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcat.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: rodrigoa <rodrigoa@student.42madrid.c      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/16 14:33:51 by rodrigoa          #+#    #+#             */
/*   Updated: 2026/01/27 15:12:05 by rodrigoa         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

size_t	ft_strlcat(char *dst, const char *src, size_t size)
{
	size_t	index;
	size_t	counter;
	size_t	init_len;

	index = ft_strlen(dst);
	counter = 0;
	init_len = ft_strlen(dst);
	if (size == 0)
		return (size + ft_strlen(src));
	if (size <= index)
		return (size + ft_strlen(src));
	while (src[counter] && index < size - 1)
	{
		dst[index] = src[counter];
		index++;
		counter++;
	}
	dst[index] = '\0';
	return (init_len + ft_strlen(src));
}
