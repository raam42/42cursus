#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_ancient_text.py                                :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: rodrigoa <rodrigoa@student.42madrid.com>  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/07/17 15:30:00 by rodrigoa         #+#    #+#              #
#    Updated: 2026/07/17 15:30:00 by rodrigoa        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

import sys
import typing


def ft_ancient_text() -> None:
    """Reads and displays a file's content handling standard OS errors."""
    # 1. Validate command-line arguments
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    filename: str = sys.argv[1]

    # 2. Print required headers
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")

    file_obj: typing.Optional[typing.IO[str]] = None

    # 3. Attempt file operations
    try:
        # Open the file in 'r' (read) mode
        file_obj = open(filename, 'r')
        
        # Read the entire file content into memory
        content: str = file_obj.read()
        
        # Print content (avoiding double newlines if the file already has one)
        if content.endswith('\n'):
            print(content, end='')
        else:
            print(content)
            
        # Manually close the file to free up system resources
        file_obj.close()
        print(f"File '{filename}' closed.")
        
    except OSError as e:
        # Catch OS-level errors (like missing files or permission denials)
        # Python's built-in OSError formatting naturally matches the subject trace
        print(f"Error opening file '{filename}': {e}")


if __name__ == "__main__":
    ft_ancient_text()