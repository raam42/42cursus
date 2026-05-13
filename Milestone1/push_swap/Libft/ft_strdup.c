/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strdup.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandres <roandres@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/27 02:16:09 by rodri             #+#    #+#             */
/*   Updated: 2026/01/29 19:13:49 by roandres         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strdup(const char *s)
{
	size_t	i;
	size_t	slen;
	char	*str;
	char	*s2;

	i = 0;
	slen = ft_strlen ((char *)s) + 1;
	str = malloc (slen * sizeof(char));
	if (str == NULL)
		return (NULL);
	s2 = (char *) s;
	while (s2[i] != '\0')
	{
		str[i] = s2[i];
		i++;
	}
	str[i] = '\0';
	return (str);
}
