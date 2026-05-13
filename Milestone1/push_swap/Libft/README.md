
*This project has been created as part of the 42 curriculum by roandres.*

## Description

This project is part of the 42 academic curriculum and aims to develop fundamental programming skills through hands-on practice. Its main objective is to apply core concepts such as problem solving, algorithmic thinking, and clean code principles while respecting the norms and requirements of 42.

The project serves both as a technical exercise and as a foundation for more advanced projects, focusing on correctness, efficiency, and code organization.

## Instructions

### Downloading the project
First, clone the repository from Git using the following command:

```bash
git clone <repository_url>
````

Then, move into the project directory:

```bash
cd <repository_name>
```

### Compilation

Ensure that you have a compatible compiler installed (such as `gcc` or `clang`) and that `make` is available on your system.
To compile the project, run:

```bash
make
```

This command will generate the executable file.

### Execution

This project builds a static library called `libft.a`. Since the library is composed only of functions, it does not include a `main` function and therefore cannot be executed directly.

To test the functions, the user must create their own `main.c` file and link it with `libft.a`.

Example workflow:

1. Compile the library:
```bash
make
````

2. Create a `main.c` file that includes `libft.h` and uses the desired functions.

3. Compile your test program linking the library:

```bash
cc main.c libft.a -o test_program
```

4. Run the executable:

```bash
./test_program
```

This allows the user to test and use the functions provided by `libft` in their own programs.

### Cleaning

To remove object files:

```bash
make clean
```

To remove all compiled files, including the executable:

```bash
make fclean
```

## Resources

### References

* Official documentation of the programming language used.
* Manual pages (`man gcc`, `man make`, etc.).
* Educational materials provided by 42.
* Online articles and tutorials related to the project topic.

### Use of Artificial Intelligence

Artificial Intelligence has been used as a supporting tool to:

* Clarify theoretical concepts.
* Provide general guidance on problem-solving approaches.

AI was not used to generate the final project code, but rather as an auxiliary resource to improve understanding and documentation, usually when the model peer to peer was not possible.