# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_alembic_2.py                                   :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: rodrigoa <rodrigoa@student.42madrid.com>  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/07/24 18:46:30 by rodrigoa         #+#    #+#              #
#    Updated: 2026/07/24 19:29:01 by rodrigoa        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
import alchemy.elements


if __name__ == "__main__":
    print("=== Alembic 2 ===\n"
          "Accessing alchemy/elements.py using 'import ...' structure\n"
          f"Testing create_earth: {alchemy.elements.create_earth()}")
