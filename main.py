# main.py
# This file is NOT the main entry point of the program, it is mostly used as a test file for logic.
# For functioning programs go to: stats_returner.py, 
from creature_card import CreatureCard
from decks import test_deck, test_deck_dict
from basic_land_card import ManaPool


def cast_card(player_mana_pool, card):
    if hasattr(card, 'mana_cost') and isinstance(card.mana_cost, list):
        # For cards with a mana_cost attribute as a list (like basic lands)
        for color in card.mana_cost:
            if not player_mana_pool.spend_mana(color, 1):
                print(f"Not enough {color} mana to cast {card.name}.")
                return False
    elif hasattr(card, 'mana_cost'):
        # For cards with a mana_cost attribute
        for color, amount in card.mana_cost.items():
            if not player_mana_pool.spend_mana(color, amount):
                print(f"Not enough {color} mana to cast {card.name}.")
                return False
    else:
        # If the card has no mana_cost attribute
        print(f"{card.name} has no mana cost.")
        return False

    print(f"{card.name} cast successfully.")
    return True


player1_mana_pool = ManaPool()
player1_mana_pool.add_mana("R", 1)
cast_card(player1_mana_pool, test_deck_dict["test_creature1_dict"])
