*This project was developed as part of the 42 curriculum by rodrigoa.*

# 📘 ft_printf

***

## 📖 Description

**ft_printf** is a custom implementation of the standard C library function `printf`. 

The goal of this project is to master **variadic functions** and understand how arguments are handled on the stack. This implementation mimics the original `printf` for the mandatory specifiers while adhering strictly to **The Norm v4.1**.



The project involves:
* Managing variable numbers of arguments using `<stdarg.h>`.
* Parsing format strings to identify specifiers.
* Converting different data types (integers, pointers, hex) into strings.
* Tracking and returning the total number of characters printed.

***

## ✅ Function Prototype
```c
int ft_printf(const char *format, ...);
```

## 🔁 Behaviour
Each call to ft_printf:

+ Processes the format string and identifies % specifiers.
+ Retrieves arguments using va_start, va_arg, and va_end.
+ Returns the total number of characters printed.
+ Returns -1 if the format string is NULL.

***

## 📦 Supported Specifiers

| Specifier | Description |
| :--- | :--- |
| `%c` | Prints a single character. |
| `%s` | Prints a string (standard C convention). |
| `%p` | Prints a `void *` pointer argument in hexadecimal format. |
| `%d` | Prints a decimal (base 10) number. |
| `%i` | Prints an integer in base 10. |
| `%u` | Prints an unsigned decimal (base 10) number. |
| `%x` | Prints a number in hexadecimal (base 16) lowercase format. |
| `%X` | Prints a number in hexadecimal (base 16) uppercase format. |
| `%%` | Prints a percent sign. |

***
## 🗂️ Project Files
The library is built using the following core files:  
+ ft_printf.c: Main entry point and dispatcher logic.
+ ft_printf_utils.c: Basic printing utilities (char and string).
+ ft_printf_numbers.c: Logic for decimal, unsigned, and hexadecimal conversions.
+ ft_printf_ptr.c: Specific logic for memory addresses (handling (nil) for NULL).

***
## 🛠️ Instructions
CompilationThe project includes a Makefile that compiles the library libftprintf.a. It is designed to automatically compile your libft dependency and avoid relinking.
```Bash
make        # Compiles the library
make clean  # Removes object files
make fclean # Removes object files and libftprintf.a
make re     # Rebuilds the entire project
```

## Usage
To use the library in your code, include the header and link the library during compilation:
```C
#include "ft_printf.h"
```
```Bash
cc main.c libftprintf.a -o my_program
```

## 🌟 Testing
To verify the project during evaluation, you can use this hardcoded main.c. It compares the output and return values of ft_printf against the standard library version.
```C
#include "ft_printf.h"
#include <stdio.h>
#include <limits.h>

int main(void)
{
    int ft_len;
    int std_len;

    printf("--- 42 MADRID FT_PRINTF TESTER ---\n\n");

    // Test: Basic Types
    ft_len = ft_printf("Mine: %c %s %u %%%%\n", 'G', "42 Madrid", 4294967295U);
    std_len = printf("Real: %c %s %u %%%%\n", 'G', "42 Madrid", 4294967295U);
    printf("Return -> Mine: %d | Real: %d\n\n", ft_len, std_len);

    // Test: Hex and Pointers
    ft_len = ft_printf("Mine: %x %X %p\n", 255, 255, &ft_len);
    std_len = printf("Real: %x %X %p\n", 255, 255, &ft_len);
    printf("Return -> Mine: %d | Real: %d\n\n", ft_len, std_len);

    // Test: Edge Cases (NULL and Limits)
    ft_len = ft_printf("Mine: %p %d %i\n", NULL, INT_MIN, INT_MAX);
    std_len = printf("Real: %p %d %i\n", NULL, INT_MIN, INT_MAX);
    printf("Return -> Mine: %d | Real: %d\n", ft_len, std_len);

    return (0);
}
```

***
## 📚 Resources
  + The Norm v4.1: Strict adherence to 42 coding standards.
  + Variadic Functions: Understanding stdarg.h for C
  + Base Conversion Logic: