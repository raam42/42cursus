/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strchr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: rodrigoa <rodrigoa@student.42madrid.c      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/16 15:04:03 by rodrigoa          #+#    #+#             */
/*   Updated: 2026/01/29 13:45:36 by rodrigoa         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

char	*ft_strchr(const char *str, int symb)
{
	while (*str)
	{
		if (*str == (char)symb)
			return ((char *)str);
		str++;
	}
	if ((char)symb == *str)
		return ((char *)str);
	return (NULL);
}
