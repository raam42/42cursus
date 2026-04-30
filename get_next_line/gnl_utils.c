#include "get_next_line.h"

size_t    ft_strlen(const char *s)
{
    size_t    i;

    if (!s)
        return (0);
    i = 0;
    while (s[i])
        i++;
    return (i);
}

char    *ft_strchr(const char *s, int c)
{
    size_t    i;

    if (!s)
        return (NULL);
    i = 0;
    while (s[i])
    {
        if (s[i] == (char)c)
            return ((char *)&s[i]);
        i++;
    }
    if (c == '\0')
        return ((char *)&s[i]);
    return (NULL);
}

char    *ft_strjoin(char *s1, char *s2)
{
    char    *res;
    size_t    i;
    size_t    j;

    if (!s1 && !s2)
        return (NULL);
    res = malloc(ft_strlen(s1) + ft_strlen(s2) + 1);
    if (!res)
        return (NULL);
    i = 0;
    j = 0;
    while (s1 && s1[i])
    {
        res[i] = s1[i];
        i++;
    }
    while (s2 && s2[j])
        res[i++] = s2[j++];
    res[i] = '\0';
    free(s1);
    return (res);
}

char    *ft_substr(char *s, unsigned int start, size_t len)
{
    char    *sub;
    size_t    i;
    size_t    s_len;

    if (!s)
        return (NULL);
    s_len = ft_strlen(s);
    if (start >= s_len)
        len = 0;
    if (len > s_len - start)
        len = s_len - start;
    sub = malloc(len + 1);
    if (!sub)
        return (NULL);
    i = 0;
    while (i < len)
    {
        sub[i] = s[start + i];
        i++;
    }
    sub[i] = '\0';
    return (sub);
}
