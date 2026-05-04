#include "get_next_line.h"
#include <stdio.h>
#include <fcntl.h>

int main(int argc, char **argv)
{
    int     fd;
    char    *line;
    int     line_count;

    line_count = 1;
    if (argc == 1)
    {
        printf("Reading from standard input (Type text, Ctrl+D to stop):\n");
        fd = 0;
    }
    else if (argc == 2)
    {
        fd = open(argv[1], O_RDONLY);
        if (fd < 0)
        {
            perror("Error opening file");
            return (1);
        }
        printf("Reading from file: %s\n", argv[1]);
    }
    else
    {
        printf("Usage: %s [filename]\n", argv[0]);
        return (1);
    }

    while ((line = get_next_line(fd)) != NULL)
    {
        printf("Line %d: %s", line_count++, line);
        free(line);
    }
    if (fd != 0)
        close(fd);
    return (0);
}
