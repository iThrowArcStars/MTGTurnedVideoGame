# main.py
import textwrap
import random
from decks import dragon_deck

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

loops = 10000

if __name__ == "__main__":
    total_draw_counts = {card.name: 0 for card in dragon_deck if hasattr(card, 'name')}

    for _ in range(loops):
        drawn_hand = draw_seven_cards(dragon_deck)
        for card in drawn_hand:
            total_draw_counts[card.name] += 1

    for card_name, draw_count in total_draw_counts.items():
        draw_count_percent = round((draw_count / (loops * 7)) * 100, 2)
        print(f"{card_name}: {draw_count_percent}%")
