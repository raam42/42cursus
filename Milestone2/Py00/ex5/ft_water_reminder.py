# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_water_reminder.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rodrigoa <rodrigoa@student.42madrid.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/17 17:18:31 by rodrigoa          #+#    #+#              #
#    Updated: 2026/05/17 17:20:26 by rodrigoa         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
def ft_water_reminder():
    last = int(input("Days since last watering: "))
    if last > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
