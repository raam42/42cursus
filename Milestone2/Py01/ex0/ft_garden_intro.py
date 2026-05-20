#!/bin/python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_garden_intro.py                                :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: rodrigoa <rodrigoa@student.42madrid.com>  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/05/20 13:50:35 by rodrigoa         #+#    #+#              #
#    Updated: 2026/05/20 13:50:35 by rodrigoa        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

def ft_garden_intro() -> None:
    name: str = "Yggrasil"
    height: str = "75km"
    age: str = "3000 years"
    print("=== Welcome to My Garden ===")
    print(f"Plant: {name}\nHeight: {height}\nAge: {age}\n")
    print("=== End of Program ===")


if __name__ == "__main__":
    ft_garden_intro()
