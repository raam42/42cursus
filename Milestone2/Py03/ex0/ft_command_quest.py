#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_command_quest.py                               :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: rodrigoa <rodrigoa@student.42madrid.com>  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/07/17 12:55:00 by rodrigoa         #+#    #+#              #
#    Updated: 2026/07/17 12:55:00 by rodrigoa        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

import sys


def ft_command_quest() -> None:
    """Parses and displays command-line arguments using sys.argv."""
    print("Command Quest ===")
    
    # sys.argv is a list of strings. Index 0 is always the program name.
    program_name: str = sys.argv[0]
    total_args: int = len(sys.argv)
    args_received: int = total_args - 1

    print(f"Program name: {program_name}")

    # Check if any extra arguments were passed beyond the script name
    if args_received == 0:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {args_received}")
        # Loop starting from index 1 to skip printing the program name again
        for i in range(1, total_args):
            print(f"Argument {i}: {sys.argv[i]}")

    print(f"Total arguments: {total_args}")


if __name__ == "__main__":
    ft_command_quest()