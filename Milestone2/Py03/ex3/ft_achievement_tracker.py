#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_achievement_tracker.py                         :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: rodrigoa <rodrigoa@student.42madrid.com>  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/07/17 14:00:00 by rodrigoa         #+#    #+#              #
#    Updated: 2026/07/17 14:00:00 by rodrigoa        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

import random


def gen_player_achievements() -> set[str]:
    """Generates a random set of unique achievements for a player."""
    achievements_pool: list[str] = [
        'Crafting Genius', 'Strategist', 'World Savior', 'Speed Runner',
        'Survivor', 'Master Explorer', 'Treasure Hunter', 'Unstoppable',
        'First Steps', 'Collector Supreme', 'Untouchable', 'Sharp Mind',
        'Boss Slayer', 'Hidden Path Finder'
    ]
    
    # Pick a random number of achievements (between 4 and 9 to ensure overlap)
    num_achievements = random.randint(4, 9)
    
    # random.sample selects unique items from the list
    chosen_achievements = random.sample(achievements_pool, num_achievements)
    
    return set(chosen_achievements)


def ft_achievement_tracker() -> None:
    """Analyzes achievement data using set operations."""
    print("=== Achievement Tracker System ===")
    
    # Generate sets for at least 4 different players
    players: dict[str, set[str]] = {
        "Alice": gen_player_achievements(),
        "Bob": gen_player_achievements(),
        "Charlie": gen_player_achievements(),
        "Dylan": gen_player_achievements()
    }
    
    for name, achievements in players.items():
        print(f"Player {name}: {achievements}")
        
    print()
    
    # 1. Track unique achievements among ALL players (Union)
    all_distinct = set().union(*players.values())
    print(f"All distinct achievements: {all_distinct}")
    
    # 2. Find achievements shared by ALL players (Intersection)
    common_achievements = set.intersection(*players.values())
    print(f"Common achievements: {common_achievements}")
    
    # 3. For each player, spot the achievements no one else has (Difference)
    for name, ach in players.items():
        # Combine everyone else's achievements into one massive set
        others_union = set()
        for other_name, other_ach in players.items():
            if name != other_name:
                others_union = others_union.union(other_ach)
        
        # Find what the current player has that the others don't
        exclusive = ach.difference(others_union)
        print(f"Only {name} has: {exclusive}")
        
    # 4. For each player, list the missing achievements to have them all
    for name, ach in players.items():
        missing = all_distinct.difference(ach)
        print(f"{name} is missing: {missing}")


if __name__ == "__main__":
    ft_achievement_tracker()