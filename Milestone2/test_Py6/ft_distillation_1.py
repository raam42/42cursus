# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_distillation_1.py                              :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: rodrigoa <rodrigoa@student.42madrid.com>  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/07/24 19:31:52 by rodrigoa         #+#    #+#              #
#    Updated: 2026/07/24 20:19:20 by rodrigoa        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
import alchemy


if __name__ == "__main__":
    print("=== Distillation 1 ===\n"
          "Using: 'import alchemy' struccture to access potions\n"
          f"Testing strength_potion: {alchemy.strength_potion()}\n"
          f"Testing heal alias: {alchemy.heal1()}")
