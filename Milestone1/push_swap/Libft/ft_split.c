/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: roandres <roandres@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/27 14:18:51 by rodri             #+#    #+#             */
/*   Updated: 2026/02/03 02:50:51 by roandres         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static void	free_all(char **ptr, size_t j)
{
	size_t	i;

	i = 0;
	while (i < j)
	{
		free(ptr[i]);
		i++;
	}
	free(ptr);
}

static size_t	word_count(char const *s, char c)
{
	size_t	i;
	size_t	count;

	i = 1;
	count = 0;
	if (s[0] != c && s[0] != '\0')
		count++;
	while (s[i] != '\0')
	{
		if (s[i] != c && s[i - 1] == c)
			count++;
		i++;
	}
	return (count);
}

static void	variables(size_t *i, size_t *j, int *start)
{
	*i = 0;
	*j = 0;
	*start = -1;
}

static char	**split_logic(char const *s, char c)
{
	size_t	i;
	size_t	j;
	int		start;
	char	**ptr;

	variables(&i, &j, &start);
	ptr = malloc((word_count(s, c) + 1) * sizeof(char *));
	if (!ptr)
		return (NULL);
	while (j < word_count(s, c))
	{
		if (s[i] != c && start == -1)
			start = i;
		if (start != -1 && (s[i] == c || s[i] == '\0'))
		{
			ptr[j] = ft_substr(s, start, i - start);
			if (!ptr[j])
				return (free_all(ptr, j), NULL);
			start = -1;
			j++;
		}
		i++;
	}
	ptr[j] = NULL;
	return (ptr);
}

char	**ft_split(char const *s, char c)
{
	char	**ptr;

	if (!s)
		return (NULL);
	if (c == '\0')
	{
		if (!s[0])
		{
			ptr = malloc(sizeof(char *));
			if (!ptr)
				return (NULL);
			ptr[0] = NULL;
			return (ptr);
		}
		ptr = malloc(2 * sizeof(char *));
		if (!ptr)
			return (NULL);
		ptr[0] = ft_substr(s, 0, ft_strlen(s));
		if (!ptr[0])
			return (free(ptr), NULL);
		ptr[1] = NULL;
		return (ptr);
	}
	return (split_logic(s, c));
}
