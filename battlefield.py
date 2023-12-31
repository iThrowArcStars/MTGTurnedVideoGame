#This file defines the battlefield mechanic in MTG
#The .remove() func only removes one instance of the requested card - dev note

# battlefield.py
class Battlefield:
    def __init__(self, card_list=None):
        self.card_list = card_list if card_list is not None else []

    def add(self, card_instance, player_mana_pool):
        for color, cost in card_instance.mana_cost.items():
            if player_mana_pool.mana.get(color, 0) < cost:
                print(f"Not enough {color} mana to cast {card_instance.card_name}.")
                return  # Exit the method if not enough mana for any color

        # If we reach here, the player has enough mana for all colors
        self.card_list.append(card_instance)
        print(f"{card_instance.card_name} successfully added to the battlefield.")

    def print_battlefield(self):
        print(self.card_list)