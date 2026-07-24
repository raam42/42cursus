# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_alembic_3.py                                   :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: rodrigoa <rodrigoa@student.42madrid.com>  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/07/24 18:49:06 by rodrigoa         #+#    #+#              #
#    Updated: 2026/07/24 18:50:55 by rodrigoa        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
from alchemy.elements import create_air


if __name__ == "__main__":
    print("=== Alembic 3 ===\n"
          "Accessing alchemy/elements.py"
          "using 'from ... import ...' structure\n"
          f"Testing create_air: {create_air()}")
