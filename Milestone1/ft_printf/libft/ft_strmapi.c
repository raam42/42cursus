/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strmapi.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: rodrigoa <rodrigoa@student.42madrid.c      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/21 13:31:08 by rodrigoa          #+#    #+#             */
/*   Updated: 2026/01/27 15:02:19 by rodrigoa         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

char	*ft_strmapi(char const *s, char (*f)(unsigned int, char))
{
	char	*result;
	size_t	i;

	i = 0;
	result = (char *)malloc(sizeof(char) * ft_strlen(s) + 1);
	if (!result || !s)
		return (NULL);
	while (i < ft_strlen(s))
	{
		result[i] = (*f)(i, s[i]);
		i++;
	}
	result[i] = 0;
	return (result);
}
