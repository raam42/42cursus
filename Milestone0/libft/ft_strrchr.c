/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strrchr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: rodrigoa <rodrigoa@student.42madrid.c      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/16 15:13:58 by rodrigoa          #+#    #+#             */
/*   Updated: 2026/01/29 15:27:11 by rodrigoa         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

char	*ft_strrchr(const char *str, int symb)
{
	int	index;

	index = (int)ft_strlen(str);
	if (!((unsigned char)symb))
		return ((char *)&str[index]);
	while (index >= 0)
	{
		if (str[index] == (unsigned char)symb)
			return ((char *)&str[index]);
		index--;
	}
	return (NULL);
}
