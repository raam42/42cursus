/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strtrim.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandres <roandres@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/27 03:39:47 by rodri             #+#    #+#             */
/*   Updated: 2026/02/03 02:51:28 by roandres         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static int	is_in_set(char c, char const *set)
{
	size_t	i;

	i = 0;
	while (set[i] != '\0')
	{
		if (set[i] == c)
		{
			return (1);
		}
		i++;
	}
	return (0);
}

char	*write_res(size_t start, size_t end, char *res, const char *s1)
{
	size_t	i;

	i = 0;
	while (start <= end)
		res[i++] = s1[start++];
	res[i] = '\0';
	return (res);
}

char	*ft_strtrim(const char *s1, const char *set)
{
	size_t	start;
	size_t	end;
	char	*res;

	start = 0;
	if (!s1 || !set)
		return (NULL);
	end = ft_strlen(s1);
	if (end == 0)
		return (ft_strdup(""));
	while (s1[start] && is_in_set(s1[start], set))
		start++;
	if (start == end)
		return (ft_strdup(""));
	end--;
	while (end > start && is_in_set(s1[end], set))
		end--;
	res = (char *)malloc(end - start + 2);
	if (!res)
		return (NULL);
	res = write_res(start, end, res, s1);
	return (res);
}
