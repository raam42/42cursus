/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memmove.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: rodrigoa <rodrigoa@student.42madrid.c      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/19 14:10:25 by rodrigoa          #+#    #+#             */
/*   Updated: 2026/01/26 16:00:16 by rodrigoa         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

void	*ft_memmove(void *dest, const void *src, size_t n)
{
	unsigned char	*tdest;
	unsigned char	*tsrc;

	tdest = (unsigned char *)dest;
	tsrc = (unsigned char *)src;
	if (!tdest && !tsrc)
		return (NULL);
	if (tsrc > tdest)
		return (ft_memcpy(tdest, tsrc, n));
	else
	{
		while (n--)
			tdest[n] = tsrc[n];
	}
	return (tdest);
}
