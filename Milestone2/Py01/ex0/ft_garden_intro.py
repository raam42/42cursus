# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_intro.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rodrigoa <rodrigoa@student.42madrid.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/17 19:17:25 by rodrigoa          #+#    #+#              #
#    Updated: 2026/05/17 19:40:35 by rodrigoa         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_garden_intro() -> None:
    name: str = "Rose"
    height: str = "25cm"
    age: str = "30 days"

    print("=== Welcome to My Garden ===")
    print(f"Plant: {name}\nHeight: {height}\nAge: {age}\n")
    print("=== End of Program ===")


if __name__ == "__main__":
    ft_garden_intro()
