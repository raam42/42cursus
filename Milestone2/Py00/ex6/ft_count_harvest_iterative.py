# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_iterative.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rodrigoa <rodrigoa@student.42madrid.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/17 18:23:38 by rodrigoa          #+#    #+#              #
#    Updated: 2026/05/17 18:26:18 by rodrigoa         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_iterative():
    target = int(input("Days until harvest: "))

    for i in range(1, target + 1):
        print(f"Day {i}")
    print("Harvest time!")
