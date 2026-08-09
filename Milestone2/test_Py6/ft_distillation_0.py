# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_distillation_0.py                              :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: rodrigoa <rodrigoa@student.42madrid.com>  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/07/24 19:26:41 by rodrigoa         #+#    #+#              #
#    Updated: 2026/07/24 20:26:34 by rodrigoa        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
from alchemy import heal1, strength_potion


if __name__ == "__main__":
    print("=== Distillation 0 ===\n"
          f"Testing strenght_potion: {strength_potion()}\n"
          f"Testing healing_portion: {heal1()}")
