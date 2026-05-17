# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_age.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rodrigoa <rodrigoa@student.42madrid.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/17 16:39:22 by rodrigoa          #+#    #+#              #
#    Updated: 2026/05/17 16:48:21 by rodrigoa         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_plant_age():
    ready = "Plant is ready to harvest!"
    not_yet = "Plant needs more time to grow."

    age_days = int(input("Enter plant age in days: "))

    if (age_days > 60):
        print(f"{ready}")
    print(f"{not_yet}")
