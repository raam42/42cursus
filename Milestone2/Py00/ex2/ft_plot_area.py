# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plot_area.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rodrigoa <rodrigoa@student.42madrid.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/17 15:32:24 by rodrigoa          #+#    #+#              #
#    Updated: 2026/05/17 15:32:45 by rodrigoa         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
def ft_plot_area():
    lenght_str = input("Enter the lenght: ")
    width_str = input("Enter the width: ")

    area = int(lenght_str) * int(width_str)
    print(f"Plot area: {area}")

