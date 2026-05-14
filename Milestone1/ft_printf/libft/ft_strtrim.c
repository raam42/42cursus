/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strtrim.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: rodrigoa <rodrigoa@student.42madrid.c      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/19 15:30:17 by rodrigoa          #+#    #+#             */
/*   Updated: 2026/01/29 15:07:04 by rodrigoa         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

char	*ft_strtrim(char const *s1, char const *set)
{
	int	index;
	int	counter;

	index = 0;
	counter = ft_strlen(s1) - 1;
	if (!s1 || !set || s1[0] == '\0')
		return (ft_strdup(""));
	while (s1[index] && ft_strchr(set, (int)s1[index]))
		index++;
	while (counter > index && ft_strrchr(set, (int)s1[counter]))
		counter --;
	if (counter < index)
		return (ft_strdup(""));
	return (ft_substr(s1, index, counter - index + 1));
}
