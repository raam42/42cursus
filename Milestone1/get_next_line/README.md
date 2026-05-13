*This project was developed as part of the 42 curriculum by rodrigoa.*

# 📘 get\_next\_line

***

## 📖 Description

**get\_next\_line** is a function that reads a file descriptor **line by line**, returning one line per call.

A “line” is defined as a sequence of characters ending with a newline character (`\n`), except possibly the last line of a file if it does not end with one.

The goal of this project is to deepen understanding of:

*   file descriptors
*   static variables
*   memory allocation
*   buffered I/O in C

***

## ✅ Function Prototype

```c
char *get_next_line(int fd);
```

***

## 🔁 Behaviour

Each call to `get_next_line`:

*   reads from the given file descriptor `fd`
*   returns the **next line**, including the trailing `\n` (if present)
*   returns `NULL` when:
    *   the end of the file is reached, or
    *   an error occurs

The caller is responsible for freeing the returned string.

***

## 📦 BUFFER\_SIZE

The read buffer size is controlled by the `BUFFER_SIZE` macro.

It can be defined at compile time:

```bash
cc -D BUFFER_SIZE=42 ...
```

If `BUFFER_SIZE` is **not** defined during compilation, it defaults to `42`.

The implementation is fully independent of the value of `BUFFER_SIZE` and works correctly with:

*   very small values (e.g. `1`)
*   large values
*   any valid positive buffer size

***

## 🗂️ Project Files

Mandatory files:

*   `get_next_line.c`  
    Core logic of the function.

*   `get_next_line_utils.c`  
    Utility functions (`ft_strlen`, `ft_strchr`, `ft_strjoin`, `ft_substr`).

*   `get_next_line.h`  
    Function prototypes, includes, and macro definitions.

***

## ⚙️ Compilation

A Makefile is provided to compile the project into a static library:

```bash
make
```

This produces:

```text
get_next_line.a
```

Standard rules are also available:

```bash
make clean
make fclean
make re
```

***

## 🧠 Implementation Notes

*   The function uses **a single static variable** to store leftover data between calls.
*   Memory is allocated and freed dynamically to avoid leaks.
*   Only the following functions are used, as required by the subject:
    *   `read`
    *   `malloc`
    *   `free`
*   No `libft` functions are used.

***

## 🧪 Testing

You can test the function using a simple `main.c` program. Here is an example that reads from a file named `text.txt` and prints each line clearly enclosed in brackets to visualize where the line cuts occur:

```c
#include "get_next_line.h"
#include <stdio.h>
#include <fcntl.h>

int main(void)
{
    int i;
    char *line;

    i = open("text.txt", O_RDONLY);
    while ((line = get_next_line(i)) != NULL)
    {
        printf("GNL returned: [%s]\n", line);
        free(line);
    }
    close(i);
    return (0);
}
```

***

## 🌟 Testing the Bonus

The bonus part of this project requires `get_next_line` to handle multiple file descriptors simultaneously, using only **one static variable**, without losing the reading state of any of them.

To verify this behavior, you can alternate reading from multiple file descriptors in a single run. By opening different files (`text.txt`, `text1.txt`, and `text2.txt`), you get distinct file descriptors, each with its own independent read offset. Notice the `while` loops at the end; these are used to drain the remaining lines and cleanly free the static variables to prevent memory leaks!

```c
#include "get_next_line_bonus.h"
#include <stdio.h>
#include <fcntl.h>

int main(void)
{
    int fd1, fd2, fd3;
    char *line;

    fd1 = open("text.txt", O_RDONLY);
    fd2 = open("text1.txt", O_RDONLY);
    fd3 = open("text2.txt", O_RDONLY);

    line = get_next_line(fd1);
    printf("FD1: [%s]\n", line);
    free(line);

    line = get_next_line(fd2);
    printf("FD2: [%s]\n", line);
    free(line);

    line = get_next_line(fd3);
    printf("FD3: [%s]\n", line);
    free(line);

    line = get_next_line(fd1);
    printf("FD1 next line: [%s]\n", line);
    free(line);

    while ((line = get_next_line(fd1)) != NULL)
        free(line);
    while ((line = get_next_line(fd2)) != NULL)
        free(line);
    while ((line = get_next_line(fd3)) != NULL)
        free(line);

    close(fd1);
    close(fd2);
    close(fd3);
    return (0);
}
```