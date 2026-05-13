/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: rodrigoa <rodrigoa@student.42madrid.c      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/19 15:45:31 by rodrigoa          #+#    #+#             */
/*   Updated: 2026/01/30 15:36:03 by rodrigoa         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

static size_t	ft_wordcount(const char *str, int c)
{
	size_t	words;
	int		i;

	words = 0;
	i = 0;
	while (*str)
	{
		if (*str != c && i == 0)
		{
			i = 1;
			words++;
		}
		else if (*str == c)
			i = 0;
		str++;
	}
	return (words);
}

static char	*ft_wordsplit(const char *str, size_t len)
{
	char	*word;

	word = (char *)malloc(len + 1);
	if (!word)
		return (NULL);
	ft_memcpy(word, str, len);
	word[len] = '\0';
	return (word);
}

static void	free_array(char **array, size_t j)
{
	while (j > 0)
		free(array[--j]);
	free(array);
}

static int	fill_array(char **array, const char *str, char c)
{
	size_t	i;
	size_t	j;
	size_t	start;

	i = 0;
	j = 0;
	while (str[i])
	{
		while (str[i] == c)
			i++;
		if (str[i] == '\0')
			break ;
		start = i;
		while (str[i] && str[i] != c)
			i++;
		array[j] = ft_wordsplit((str + start), (i - start));
		if (!array[j])
			return (free_array(array, j), -1);
		j++;
	}
	array[j] = NULL;
	return (0);
}

char	**ft_split(char const *s, char c)
{
	char	**str;

	if (!s)
		return (0);
	str = (char **)ft_calloc((ft_wordcount(s, c) + 1), sizeof(char *));
	if (!str)
		return (0);
	if (fill_array(str, s, c) == -1)
		return (0);
	return (str);
}
