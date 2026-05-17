# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_recursive.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rodrigoa <rodrigoa@student.42madrid.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/17 17:33:24 by rodrigoa          #+#    #+#              #
#    Updated: 2026/05/17 18:26:43 by rodrigoa         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_recursive(current=1, target=None):
    if target is None:
        target = int(input("Days until harvest: "))

    if current > target:
        print("Harvest time!")
        return

    print(f"Day {current}")

    ft_count_harvest_recursive(current + 1, target)
