#include "get_next_line.h"

static char	*read_to_stash(int fd, char *stash)
{
	char	*buf;
	ssize_t	bytes;
	char	*tmp;

	buf = malloc(BUFFER_SIZE + 1);
	if (!buf)
		return (free(stash), NULL);
	bytes = 1;
	while ((!stash || !ft_strchr(stash, '\n')) && bytes > 0)
	{
		bytes = read(fd, buf, BUFFER_SIZE);
		if (bytes < 0)
		{
			free(buf);
			return (free(stash), NULL);
		}
		buf[bytes] = '\0';
		if (bytes > 0)
		{
			if (!stash)
				tmp = ft_strdup(buf);
			else
				tmp = ft_strjoin(stash, buf);
			free(stash);
			if (!tmp)
				return (free(buf), NULL);
			stash = tmp;
		}
	}
	free(buf);
	return (stash);
}

static char	*extract_line(char *stash)
{
	size_t	i;
	size_t	len;

	if (!stash || !stash[0])
		return (NULL);
	i = 0;
	while (stash[i] && stash[i] != '\n')
		i++;
	len = i;
	if (stash[i] == '\n')
		len++;
	return (ft_substr(stash, 0, len));
}

static char	*stash_after_line(char *stash)
{
	size_t	i;
	size_t	len;
	char	*new_stash;

	i = 0;
	while (stash[i] && stash[i] != '\n')
		i++;
	if (!stash[i])
		return (free(stash), NULL);
	i++;
	len = ft_strlen(stash + i);
	new_stash = ft_substr(stash, (unsigned int)i, len);
	free(stash);
	return (new_stash);
}

char	*get_next_line(int fd)
{
	static char	*stash[1024];
	char		*line;

	if (fd < 0 || fd >= 1024 || BUFFER_SIZE <= 0)
		return (NULL);
	if (read(fd, 0, 0) < 0)
		return (free(stash[fd]), stash[fd] = NULL, NULL);
	stash[fd] = read_to_stash(fd, stash[fd]);
	if (!stash[fd])
		return (NULL);
	line = extract_line(stash[fd]);
	if (!line)
		return (free(stash[fd]), stash[fd] = NULL, NULL);
	stash[fd] = stash_after_line(stash[fd]);
	return (line);
}
