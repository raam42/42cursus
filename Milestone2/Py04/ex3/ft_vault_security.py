#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_vault_security.py                              :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: rodrigoa <rodrigoa@student.42madrid.com>  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/07/20 17:02:24 by rodrigoa         #+#    #+#              #
#    Updated: 2026/07/20 17:02:24 by rodrigoa        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

import typing


def secure_archive(file_name: str, action: str = "read", content: str = "") -> tuple[bool, str]:
    """
    Safely accesses a file for reading or writing using a context manager.
    Returns a tuple containing a success boolean and the file content or an error message.
    """
    try:
        if action == "read":
            # The 'with' statement automatically manages resource cleanup
            with open(file_name, 'r') as file:
                file_content: str = file.read()
                return True, file_content
                
        elif action == "write":
            with open(file_name, 'w') as file:
                file.write(content)
                return True, "Content successfully written to file"
                
        else:
            return False, "Invalid action specified."

    except OSError as e:
        # Formats the error string to exactly match the subject's tuple output requirement
        return False, f"[Errno {e.errno}] {e.strerror}: '{file_name}'"


if __name__ == "__main__":
    # Test block to replicate the exact output shown in the subject example
    print("=== Cyber Archives Security ===")
    
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive('/not/existing/file', 'read'))
    
    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive('/etc/master.passwd', 'read'))
    
    print("Using 'secure_archive' to read from a regular file:")
    print(secure_archive('ancient_fragment.txt', 'read'))
    
    print("Using 'secure_archive' to write previous content to a new file:")
    print(secure_archive('new_fragment.txt', 'write', 'Content successfully written to file'))