#include "get_next_line.h"
#include <stdio.h>
#include <fcntl.h>

int main(int argc, char **argv)
{
    int     fds[1024];
    char    *line;
    int     i;
    int     files_left;

    if (argc == 1)
    {
        printf("Reading from standard input (Type text, Ctrl+D to stop):\n");
        while ((line = get_next_line(0)) != NULL)
        {
            printf("%s", line);
            free(line);
        }
        return (0);
    }
    files_left = 0;
    for (i = 1; i < argc; i++)
    {
        fds[i] = open(argv[i], O_RDONLY);
        if (fds[i] < 0)
            perror(argv[i]);
        else
            files_left++;
    }

    while (files_left > 0)
    {
        for (i = 1; i < argc; i++)
        {
            if (fds[i] >= 0)
            {
                line = get_next_line(fds[i]);
                if (line)
                {
                    printf("File %d (%s): %s", i, argv[i], line);
                    free(line);
                }
                else
                {
                    close(fds[i]);
                    fds[i] = -1;
                    files_left--;
                }
            }
        }
    }
    return (0);
}
