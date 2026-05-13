#ifndef GET_NEXT_LINE_BONUS_H
# define GET_NEXT_LINE_BONUS_H

# include <stdlib.h>
# include <unistd.h>

/*
** BUFFER_SIZE can be defined at compilation time:
** cc -D BUFFER_SIZE=42 ...
*/
# ifndef BUFFER_SIZE
#  define BUFFER_SIZE 42
# endif

char    *get_next_line(int fd);

/*
** Utility functions (no libft allowed)
*/
size_t    ft_strlen(const char *s);
char    *ft_strchr(const char *s, int c);
char    *ft_strjoin(char *s1, char *s2);
char    *ft_substr(char *s, unsigned int start, size_t len);

#endif