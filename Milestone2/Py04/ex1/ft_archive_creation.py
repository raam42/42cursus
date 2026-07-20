#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_archive_creation.py                            :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: rodrigoa <rodrigoa@student.42madrid.com>  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/07/20 16:01:46 by rodrigoa         #+#    #+#              #
#    Updated: 2026/07/20 16:01:46 by rodrigoa        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
import sys
import typing


def ft_archive_creation() -> None:
    """Reads a file, appends '#' to each line, and optionally saves it."""
    if len(sys.argv) != 2:
        print("Usage: ft_archive_creation.py <file>")
        return

    file_name: str = sys.argv[1]
    
    # Header updated to match Exercise 1 specifications
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{file_name}'")
    print("===\n")

    try:
        # Reusing the strict file reading structure from Exercise 0
        file: typing.IO[typing.Any] = open(file_name, 'r')
        content: str = file.read()
        
        print(content)
        if content and not content.endswith('\n'):
            print()
            
        file.close()
        print("===")
        print(f"File '{file_name}' closed.\n")
        
    except OSError as e:
        print(f"Error opening file '{file_name}': [Errno {e.errno}] {e.strerror}: '{file_name}'")
        return

    # Data Transformation Step
    print("Transform data:")
    print("===\n")
    transformed_content: str = ""
    
    if content:
        lines: list[str] = content.split('\n')
        # Prevent adding a stray '#' if the file ends with a clean newline
        if len(lines) > 1 and lines[-1] == "":
            lines = lines[:-1]
        
        for line in lines:
            transformed_content += line + "#\n"
            
    print(transformed_content)

    # Saving Step using only authorized functions
    print("===")
    new_file_name: str = input("Enter new file name (or empty): ")
    
    if not new_file_name:
        print("Not saving data.")
    else:
        print(f"Saving data to '{new_file_name}'")
        try:
            # 'w' mode creates the file or replaces it if it already exists
            new_file: typing.IO[typing.Any] = open(new_file_name, 'w')
            new_file.write(transformed_content)
            new_file.close()
            print(f"Data saved in file '{new_file_name}'.\n")
        except OSError as e:
            print(f"Error opening file '{new_file_name}': [Errno {e.errno}] {e.strerror}: '{new_file_name}'")


if __name__ == "__main__":
    ft_archive_creation()