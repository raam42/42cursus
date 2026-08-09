# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_alembic_5.py                                   :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: rodrigoa <rodrigoa@student.42madrid.com>  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/07/24 18:56:06 by rodrigoa         #+#    #+#              #
#    Updated: 2026/07/24 18:57:38 by rodrigoa        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
from alchemy import create_air


if __name__ == "__main__":
    print("=== Alembic 5 ===\n"
          "Accessing the alchemy module using 'from alchemy import ...'"
          f"Testing create_air: {create_air()}")
