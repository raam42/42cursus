#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_inventory_system.py                            :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: rodrigoa <rodrigoa@student.42madrid.com>  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/07/17 14:30:00 by rodrigoa         #+#    #+#              #
#    Updated: 2026/07/17 14:30:00 by rodrigoa        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

import sys


def ft_inventory_system() -> None:
    """Parses command-line arguments to manage an RPG inventory dictionary."""
    print("=== Inventory System Analysis ===")
    
    inventory: dict[str, int] = {}
    
    # 1. Parse command-line parameters
    for arg in sys.argv[1:]:
        parts = arg.split(':')
        
        # Discard invalid syntax
        if len(parts) != 2:
            print(f"Error invalid parameter '{arg}'")
            continue
            
        item_name = parts[0]
        val_str = parts[1]
        
        # Discard redundant parameters
        if item_name in inventory.keys():
            print(f"Redundant item '{item_name}' discarding")
            continue
            
        # Try to parse the quantity
        try:
            quantity = int(val_str)
            inventory[item_name] = quantity
        except ValueError as e:
            print(f"Quantity error for '{item_name}': {e}")
            
    if not inventory:
        return

    # 2. Display the inventory
    print(f"Got inventory: {inventory}")
    
    # 3. Create and display the list of all items
    item_list = list(inventory.keys())
    print(f"Item list: {item_list}")
    
    # 4. Calculate and print total quantity
    total_items = sum(inventory.values())
    print(f"Total quantity of the {len(item_list)} items: {total_items}")
    
    # 5. Display percentage for each item
    for item in item_list:
        qty = inventory[item]
        percentage = round((qty / total_items) * 100, 1)
        # Using .1f ensures it always prints one decimal place (e.g., 25.0%)
        print(f"Item {item} represents {percentage:.1f}%")
        
    # 6. Report most and least abundant items (first from CLI in case of tie)
    most_abundant_item = ""
    most_abundant_qty = -1
    least_abundant_item = ""
    least_abundant_qty = float('inf')
    
    for item in item_list:
        qty = inventory[item]
        # Strictly greater/less than ensures we keep the first one found on ties
        if qty > most_abundant_qty:
            most_abundant_qty = qty
            most_abundant_item = item
        if qty < least_abundant_qty:
            least_abundant_qty = qty
            least_abundant_item = item
            
    print(f"Item most abundant: {most_abundant_item} "
          f"with quantity {most_abundant_qty}")
    print(f"Item least abundant: {least_abundant_item} "
          f"with quantity {least_abundant_qty}")
          
    # 7. Add a new item and display again
    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    ft_inventory_system()