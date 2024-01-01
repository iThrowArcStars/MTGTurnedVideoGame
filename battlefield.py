#battlefield.py
#This file defines the battlefield mechanic in MTG
#The .remove() func only removes one instance of the requested card - dev note

class Battlefield:
    def __init__(self, card_list=None):
        self.card_list = card_list if card_list is not None else []

    def add(self, card_instance, player_mana_pool):
        insufficient_mana_colors = []
        for color, cost in card_instance.mana_cost.items():
            if player_mana_pool.mana.get(color, 0) < cost:
                insufficient_mana_colors.append(color)

        if insufficient_mana_colors:
            print(f"Not enough {', '.join(insufficient_mana_colors)} mana to cast {card_instance.name}.")
            return

        for color, cost in card_instance.mana_cost.items():
            player_mana_pool.mana[color] -= cost

        self.card_list.append(card_instance)
        print(f"{card_instance.name} successfully added to the battlefield.")
        print(player_mana_pool.mana)
