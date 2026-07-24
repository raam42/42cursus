# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_transmutation_0.py                             :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: rodrigoa <rodrigoa@student.42madrid.com>  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/07/24 20:04:44 by rodrigoa         #+#    #+#              #
#    Updated: 2026/07/24 20:06:41 by rodrigoa        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
from alchemy.transmutation.recipes import lead_to_gold


if __name__ == "__main__":
    print("=== Transmutation 0 ===\n"
          "Using file alchemy/transmutation/recipes.py directly\n"
          f"Testing lead_to_gold: {lead_to_gold()}")
