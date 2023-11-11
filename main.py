import textwrap
import random
from all_cards import *

def print_card_info(card):
    print(f"Name: {card.name}")
    print(f"Type: {card.card_type}")

    if hasattr(card, "abilities") and card.abilities:
        print("Abilities:")
        for ability in card.abilities:
            wrapped_text = textwrap.fill(ability, width=80)  # Adjust the line width as needed
            print(f"  - {wrapped_text}")

    if hasattr(card, "mana_cost") and card.mana_cost:
        print(f"Mana Cost: {', '.join(card.mana_cost)}")

    print()

def draw_seven_cards():
    shuffled_deck = random.sample(all_cards, len(all_cards))
    hand = shuffled_deck[:7]
    return hand

if __name__ == "__main__":
    # Example: Print information for each drawn card
    drawn_cards = draw_seven_cards()

    print("Drawn Cards:")
    for card in drawn_cards:
        print_card_info(card)
