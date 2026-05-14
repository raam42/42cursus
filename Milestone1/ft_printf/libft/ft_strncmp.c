/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strncmp.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: rodrigoa <rodrigoa@student.42madrid.c      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/16 15:22:46 by rodrigoa          #+#    #+#             */
/*   Updated: 2026/01/29 14:59:02 by rodrigoa         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

int	ft_strncmp(const char *str1, const char *str2, size_t n)
{
	size_t	index;

	index = 0;
	while (str1[index] == str2[index] && str1[index] && index < n)
	{
		if (str1[index] != str2[index])
			return ((unsigned char)str1[index] - (unsigned char)str2[index]);
		index++;
	}
	if (index < n)
		return ((unsigned char)str1[index] - (unsigned char)str2[index]);
	return (0);
}
