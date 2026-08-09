# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_alembic_4.py                                   :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: rodrigoa <rodrigoa@student.42madrid.com>  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/07/24 18:51:46 by rodrigoa         #+#    #+#              #
#    Updated: 2026/07/24 18:55:41 by rodrigoa        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
import sys
import alchemy


if __name__ == "__main__":
    print("=== Alembic 4 ===\n"
          "Accessing the alchemy module using 'import alchemy'\n"
          f"Testing create_air: {alchemy.create_air()}\n"
          "Now show that not all functions can be reached\n"
          "This will raise an exception!\n"
          "Testing the hidden creat_earth: ", end="")
    sys.stdout.flush()
    print(f"{alchemy.create_earth()}")  # type: ignore[attr-defined]
