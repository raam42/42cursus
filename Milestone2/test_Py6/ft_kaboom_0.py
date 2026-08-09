# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_kaboom_0.py                                    :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: rodrigoa <rodrigoa@student.42madrid.com>  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/07/24 21:02:40 by rodrigoa         #+#    #+#              #
#    Updated: 2026/07/24 21:16:52 by rodrigoa        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
import alchemy.grimoire


if __name__ == "__main__":
    record = alchemy.grimoire.light_spell_record
    (
        'Fantasy', 'Earth, wind and fire'
    )
    print("=== Kaboom 0 ===\n"
          "Using grimoire module directly\n"
          "Testing record light spell: ", end="")
    print(record)
