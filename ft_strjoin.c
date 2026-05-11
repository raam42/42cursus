/* ************************************************************************** */
/*                                                                            */
/*   ft_strjoin.c                                                             */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strjoin(char const *s1, char const *s2)
{
	size_t	i;
	size_t	j;
	char	*endstr;

	if (!s1 || !s2)
		return (NULL);
	i = 0;
	j = 0;
	endstr = (char *)malloc(sizeof(char) * (ft_strlen(s1) + ft_strlen(s2) + 1));
	if (!endstr)
		return (NULL);
	while (s1[i])
	{
		endstr[i] = s1[i];
		i++;
	}
	while (s2[j])
		endstr[i++] = s2[j++];
	endstr[i] = '\0';
	return (endstr);
}
