/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcat.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: rodrigoa <rodrigoa@student.42madrid.c      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/07 12:22:10 by rodrigoa          #+#    #+#             */
/*   Updated: 2026/02/09 15:58:10 by rodrigoa         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

size_t	ft_strlcat(char *dst, const char *src, size_t n)
{
	size_t	i;
	size_t	j;
	size_t	init_cat;

	i = ft_strlen(dst);
	j = 0;
	init_cat = ft_strlen(dst);
	if (n == 0 || n <= i)
		return (n + ft_strlen(src));
	while (src[j] && (i < n - 1))
	{
		dst[i] = src[j];
		i++;
		j++;
	}
	dst[i] = '\0';
	return (init_cat + ft_strlen(src));
}
