# main.py
import textwrap
import random
from dragon_deck import dragon_deck

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

def draw_seven_cards(deck):
    shuffled_deck = random.sample(deck, len(deck))
    hand = shuffled_deck[:7]
    return hand

if __name__ == "__main__":
    # Example: Print information for each drawn card
    drawn_cards = draw_seven_cards(dragon_deck)

    print("Drawn Cards:")
    for card in drawn_cards:
        print_card_info(card)
