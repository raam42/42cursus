# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_alembic_1.py                                   :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: rodrigoa <rodrigoa@student.42madrid.com>  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/07/24 18:44:22 by rodrigoa         #+#    #+#              #
#    Updated: 2026/07/24 20:16:58 by rodrigoa        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
from elements import create_water


if __name__ == "__main__":
    print("=== Alembic 1 ===\n"
          "Using: 'from ... import ...' structure to access elements.py"
          f"Testing create_water: {create_water()}")
