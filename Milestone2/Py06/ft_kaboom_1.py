#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_kaboom_1.py                                    :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: rodrigoa <rodrigoa@student.42madrid.com>  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/07/24 21:20:03 by rodrigoa         #+#    #+#              #
#    Updated: 2026/07/24 21:25:25 by rodrigoa        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #


if __name__ == "__main__":
    print("=== Kaboom 1 ===\n"
          "Acces to alchemy/grimoiredark_spellbook.py directly\n"
          "Test import now THIS WILL RAISE AN UNCAUGHT EXCEPTION")
    try:
        from alchemy.grimoire import dsr  # noqa: F401
    except Exception as e:
        print(f"Exception catched: {e}")
