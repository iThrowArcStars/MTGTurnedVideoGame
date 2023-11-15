# main.py
# This file is NOT the main entry point of the program, it is mostly used as a test file for logic.
# For functioning programs go to: stats_returner.py, 
from decks import (
    test_creature1,
    test_creature2,
    test_creature3,
    test_creature4,
    test_creature5,
    test_creature6,
    test_creature7,
    test_deck
)
from basic_land_card import ManaPool

class Battlefield:
    def __init__(self):
        self.cards_on_battlefield = {}

    def add_card(self, card_instance):
        if card_instance in self.cards_on_battlefield:
            self.cards_on_battlefield[card_instance] += 1
        else:
            self.cards_on_battlefield[card_instance] = 1

    def remove_card(self, card_instance):
        if card_instance in self.cards_on_battlefield:
            if self.cards_on_battlefield[card_instance] > 1:
                self.cards_on_battlefield[card_instance] -= 1
            else:
                del self.cards_on_battlefield[card_instance]
        else:
            print("Card not found on the battlefield.")

    def cast_card(self, card_instance):
        self.add_card(card_instance)
        print(f"{card_instance} has been cast and added to the battlefield.")

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


battlefield = Battlefield()
battlefield.cast_card(test_creature1)

print(battlefield.cards_on_battlefield)