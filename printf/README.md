_This project has been created as part of the 42 curriculum by rodrigoa._

# ft_printf

## Description

**ft_printf** is a 42 core curriculum project whose goal is to reimplement the standard C library function `printf()`.

The project introduces the concept of **variadic functions** in C and requires reproducing the behaviour of `printf()` for a limited and well‑defined set of format specifiers, using only low‑level output functions.

Once completed, `ft_printf` can be integrated into **libft** and reused in future C projects.

---

## Instructions

### Compilation

Requirements:
- `cc` (or `clang`)
- `make`

Compile the library:

```bash
make
````

This builds the static library:

```text
libftprintf.a
```

***

### Usage

To use `ft_printf`, include its header and link the library:

```c
#include "ft_printf.h"
```

Example:

```c
ft_printf("Hello %s, value = %d\n", "world", 42);
```

The function returns the **number of characters printed**, exactly like the standard `printf()`.

***

## Project constraints

The implementation follows the constraints defined in the subject:

*   Only the following functions are allowed:
    *   `malloc`
    *   `free`
    *   `write`
    *   `va_start`, `va_arg`, `va_copy`, `va_end`
*   Buffer management from the original `printf()` is **not implemented**
*   Output is written directly using `write()`
*   The project is written in **C** and follows the 42 Norm
*   The output library must be created using `ar` (no `libtool`)

***

## Implemented conversions (mandatory)

The mandatory part implements the following format specifiers:

| Specifier | Description                                       |
| --------- | ------------------------------------------------- |
| `%c`      | print a single character                          |
| `%s`      | print a string of characters                      |
| `%p`      | print a pointer address in hexadecimal            |
| `%d`      | print a signed decimal integer                    |
| `%i`      | print a signed decimal integer                    |
| `%u`      | print an unsigned decimal integer                 |
| `%x`      | print an unsigned hexadecimal integer (lowercase) |
| `%X`      | print an unsigned hexadecimal integer (uppercase) |
| `%%`      | print the `%` character                           |

All conversions mirror the behaviour of the standard `printf()` for the supported specifiers.

***

## Design and implementation

The project is structured around a clear separation of responsibilities:

*   `ft_printf.c`  
    Handles format string parsing and dispatches each conversion.
*   Conversion helper files  
    Implement one responsibility each (`char`, `string`, `integer`, `hex`, `pointer`).
*   All helper functions return the number of characters printed, allowing
    `ft_printf()` to compute its return value accurately.

This modular design improves readability, maintainability, and extensibility for the bonus part.

***

## Return value behaviour

Like the standard `printf()`, `ft_printf()` returns:

*   the total number of characters printed on success
*   `-1` in case of an error

Care is taken to count every printed character, including signs, prefixes, and literal text.

***

## Bonus part

The bonus part extends the mandatory implementation with additional formatting features, such as:

*   field width
*   precision
*   flags (`-`, `0`, `.`, `#`, `+`, space)

Bonus functionality is implemented in separate files (`*_bonus.c`) as required, and is evaluated **only if the mandatory part is fully correct**.

***

## Project structure

*   `ft_printf.c` — main dispatcher
*   `ft_print_*.c` — conversion handlers
*   `ft_printf.h` — public interface
*   `libft/` — local libft dependency
*   `Makefile` — compilation rules

***

## Use of Artificial Intelligence

Artificial Intelligence tools were used strictly as a **supporting and learning aid**, in accordance with the project guidelines:

*   to clarify theoretical concepts (variadic functions, formatted output),
*   to review design decisions and complexity,
*   to assist with documentation drafting.

All code was written, reviewed, understood, and validated by the author.

***

## Resources

*   42 ft\_printf subject [\[printf \| PDF\]](https://hasbroinc-my.sharepoint.com/personal/mejiar1_wz_hasbro_com/Documents/Microsoft%20Copilot%20Chat%20Files/printf.pdf?web=1)
*   C standard documentation on `printf` and variadic functions
*   Manual pages: `man printf`, `man stdarg`
