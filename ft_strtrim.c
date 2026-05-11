/* ************************************************************************** */
/*                                                                            */
/*   ft_strtrim.c                                                             */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strtrim(char const *s1, char const *set)
{
	size_t	i;
	size_t	j;

	if (!s1 || !set)
		return (NULL);
	i = 0;
	j = ft_strlen(s1);
	if (j == 0)
		return (ft_strdup(""));
	j = j - 1;
	while (s1[i] && ft_strchr(set, (int)s1[i]))
		i++;
	while (j > i && ft_strrchr(set, (int)s1[j]))
		j--;
	if (j < i)
		return (ft_strdup(""));
	return (ft_substr(s1, i, (j - i + 1)));
}
