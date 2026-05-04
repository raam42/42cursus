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
