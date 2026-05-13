/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strjoin.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: rodrigoa <rodrigoa@student.42madrid.c      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/19 15:20:58 by rodrigoa          #+#    #+#             */
/*   Updated: 2026/01/29 15:04:22 by rodrigoa         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"
#include <stdlib.h>

char	*ft_strjoin(char const *s1, char const *s2)
{
	int		index;
	int		counter;
	char	*endstr;

	index = 0;
	counter = 0;
	endstr = (char *)malloc(sizeof(char) * (ft_strlen(s1) + ft_strlen(s2) + 1));
	if (!s1)
		return (ft_strdup(s2));
	if (!s2)
		return (ft_strdup(s1));
	if (endstr == 0)
		return (NULL);
	while (s1[index])
	{
		endstr[index] = s1[index];
		index++;
	}
	while (s2[counter])
		endstr[index++] = s2[counter++];
	endstr[index] = 0;
	return (endstr);
}
