*This project has been created as part of the curriculum of 42 by rodrigoa.*

# ft_printf

## Description

`ft_printf` is a reimplementation of the C standard library function `printf`.
The goal of this project is to understand variadic functions, formatted output,
and low-level I/O using `write`.

The project is divided into a mandatory part, which reproduces the basic
behaviour of `printf`, and an optional bonus part, which extends the formatter
with flags, width, and precision handling.

## Instructions

### Compilation

To compile the mandatory part:

```bash
make
````

This will generate the static library:

```text
libftprintf.a
```

To compile with bonus support:

```bash
make bonus
```

### Usage

Include the header and link the library:

```c
#include "ft_printf.h"

ft_printf("Hello %s (%d)\n", "world", 42);
```

The `ft_printf` function returns the number of characters printed, or `-1` on
error.

## Algorithm and Design

The implementation is based on a format string parser that processes the input
character by character.

For the mandatory part:

*   Each conversion specifier is detected after `%`
*   A dispatcher function calls the appropriate printer (`%c`, `%s`, `%d`, etc.)
*   Output is written directly using `write`

For the bonus part:

*   The format is first parsed into a `t_format` structure
*   Flags, width, precision, and specifier are stored explicitly
*   Printing is split into small layout functions to respect La Norma limits
*   Padding, precision, and prefixes are applied in a deterministic order

The code is structured into small functions and files in order to comply with
La Norma v4 constraints (maximum number of lines, variables, and functions per
file).

## Resources

*   `man 3 printf`
*   `man stdarg`
*   GNU C Library documentation

### AI Usage

AI tools were used as a **learning and verification aid only**, mainly to:

*   review formatting edge cases
*   double-check compliance with La Norma v4
*   reason about refactoring strategies when splitting large functions

All final design decisions and implementations were written and reviewed
manually.
