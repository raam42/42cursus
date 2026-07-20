#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_stream_management.py                           :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: rodrigoa <rodrigoa@student.42madrid.com>  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/07/20 16:46:00 by rodrigoa         #+#    #+#              #
#    Updated: 2026/07/20 16:46:00 by rodrigoa        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
import sys
import typing


def ft_stream_management() -> None:
    """Demonstrates manual control of stdin, stdout, and stderr streams."""
    if len(sys.argv) != 2:
        print("Usage: ft_stream_management.py <file>")
        return

    file_name: str = sys.argv[1]
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{file_name}'")
    print("===\n")

    try:
        # Read operation (Still no 'with' statement allowed)
        file: typing.IO[typing.Any] = open(file_name, 'r')
        content: str = file.read()
        
        print(content)
        if content and not content.endswith('\n'):
            print()
            
        file.close()
        print("===")
        print(f"File '{file_name}' closed.\n")
        
    except OSError as e:
        # Redirecting the error message to stderr with the required prefix
        print(f"[STDERR] Error opening file '{file_name}': [Errno {e.errno}] {e.strerror}: '{file_name}'", file=sys.stderr)
        return

    print("Transform data:")
    print("===\n")
    transformed_content: str = ""
    
    if content:
        lines: list[str] = content.split('\n')
        if len(lines) > 1 and lines[-1] == "":
            lines = lines[:-1]
        
        for line in lines:
            transformed_content += line + "#\n"
            
    print(transformed_content)

    # Manual input handling via stdin
    print("===")
    print("Enter new file name (or empty): ", end="")
    sys.stdout.flush()  # Forces the prompt to display immediately
    
    # Readline captures the newline character from hitting 'Enter', so we strip it
    new_file_name: str = sys.stdin.readline().strip('\n')
    
    if not new_file_name:
        print("Not saving data.")
    else:
        print(f"Saving data to '{new_file_name}'")
        try:
            new_file: typing.IO[typing.Any] = open(new_file_name, 'w')
            new_file.write(transformed_content)
            new_file.close()
            print(f"Data saved in file '{new_file_name}'.")
        except OSError as e:
            # Catching the write-permission error and sending it to stderr
            print(f"[STDERR] Error opening file '{new_file_name}': [Errno {e.errno}] {e.strerror}: '{new_file_name}'", file=sys.stderr)
            print("Data not saved.")


if __name__ == "__main__":
    ft_stream_management()