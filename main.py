# main.py
import textwrap
import random
from decks import test_deck

def print_card_info(card):
    print(f"Name: {card.name}")
    print(f"Type: {card.card_type}")

    if hasattr(card, "abilities") and card.abilities:
        print("Abilities:")
        for ability in card.abilities:
            wrapped_text = textwrap.fill(ability, width=80)
            print(f"  - {wrapped_text}")

    if hasattr(card, "mana_cost") and card.mana_cost:
        print(f"Mana Cost: {', '.join(card.mana_cost)}")

    print()

def draw_seven_cards(deck):
    shuffled_deck = random.sample(deck, len(deck))
    hand = shuffled_deck[:7]
    for card in hand:
        card.draw_count += 1
    return hand


if __name__ == "__main__":
    for _ in range(10000):
        drawn_hand = draw_seven_cards(test_deck)
    
    for card in test_deck:
        print(f"{card.name}: {card.draw_count}")
