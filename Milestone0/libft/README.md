*This project was created as part of the 42 curriculum by **rodrigoa**.*

# :speaking_head: About
The aim of this project is to create our own C library containing usual functions that will be allowed to use in future projeccts.

# :book: Resources for Libft
[42-Gitbook](https://42-cursus.gitbook.io/guide)    
[C Standard Library Rewrirte](https://www.asidesigned.com/project-libft.html)   
[C Programming Languague](https://github.com/MarkosComK/42-Libft/files/14312769/C-Programming-Language-2nd-Edition.pdf)    
[Emojis](https://gist.github.com/rxaviers/7360908)  
[Makefile](https://www.cs.colby.edu/maxwell/courses/tutorials/maketutor/)   
[Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)  

### :rocket: TLDR: This project consists of manually coded C functions (see below), which are then compiled into a library for use throughout the cursus. 

## Character Testing functions 
ft_isalnum - alphanumeric character test.   
ft_isascii - test for ASCII characters.  
ft_isalpha - aphabetic character test.    
ft_isdigit - decimal digit test.    
ft_isprint - printable character test.  
ft_tolower - lower-case letter conversion.  
ft_toupper - upper-case letter conversion.
## Memory Manipulation functions    
ft_calloc - memory allocation.  
ft_bzero - write zertos to a byte string.   
ft_memcpy - copy memory area.   
ft_memchr - locate byte in byte string.  
ft_memcmp - compare byte string.    
ft_memmove - copy byte string.  
ft_memset - write a byte to byte string.
## String Manipulation Functions    
ft_strlen - find lenght of string.  
ft_strchr - locate first character occurrance in string.    
ft_strrchr - locate last character occurrance in string.    
ft_striteri - modify the original string w/specified function.  
ft_strnstr - locate substring in a string (size-bounded).   
ft_strncmp - compare strings (size-bounded).    
ft_strlcpy - size-bounded string copying.   
ft_strlcat - size-bounded string concatenation.     
ft_strdup - allocates sufficient memory for a copy of the string.
## File Descriptor Functions    
ft_putchar_fd - output a chracter to given file.    
ft_putstr_fd - output string to given file.     
ft_putendl_fd - output string to given file w/new line.     
ft_putnbr_fd - output integer to given file.
## Non-standard functions   
ft_itoa - integer to ASCII string convertion.   
ft_substr - extract substring from string.  
ft_strtrim - trim beginning to end of string w/specified characters.    
ft_strjoin - concatenate two strings into a new string (w/malloc).  
ft_split - split string, w/specified delimiter, into an array of strings.   
ft_strmapi - create a new string from modifying string w/specified function.    
## Linked lists functions
ft_lstnew - crate new list. 
ft_lstsize - count elements of list.    
ft_lstlast - find last element of list.  
ft_lstadd_back - add new element at the end of list.    
ft_lstadd_front - add new element at beggining of list.     
ft_lstdelone - delete element from list.    
ft_lstclear - delete sequence of elements of al lists.  
ft_lstiter - apply function to content of all lists.    
ft_lstmap - apply function to content of all lists' elements into a new list.   

# :hammer_and_wrench: Getting Started... 
## Requirements 
The library is written in C and thus needs the **cc compiler** and some standard **C libraries** to run.    
# Instructions  
### 1. Compiling the library    
To compile the library, run:    
~~~
$ cd path/to/libft && make
~~~
### 2. Embeding it to your code 
To use the library functions in your own code, simply include the following header:
~~~
#include "libft.h"
~~~  

# :test_tube: Testing   
If you haven't coded any testers yet and need some guidance; here are some third-party testers that you can use:
## Third-party Testers  
+ [**Francinette / Paco**](https://github.com/xicodomingues/francinette)
+ [**Libftest**](https://github.com/jtoty/Libftest)
+ [**War Machine**](https://github.com/0x050f/libft-war-machine)
+ [**Libftdestructor**](https://github.com/t0mm4rx/libftdestructor)         
