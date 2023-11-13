# main.py
import textwrap
import random
from decks import wolf_deck
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

def user_input():
    while True:
        try:
            user_input = str(input("Would you like to see the stats on Dragon Deck ('D'), or Wolf Deck ('W')"))
        except ValueError:
            print("Invalid response, try again. ")
            continue
        break
    if user_input == "D":
        return dragon_deck
    else: return wolf_deck

loops = 100000
user_input_var = user_input()

if __name__ == "__main__":
    total_draw_counts = {card.name: 0 for card in user_input_var if hasattr(card, 'name')}

    for _ in range(loops):
        drawn_hand = draw_seven_cards(user_input_var)
        for card in drawn_hand:
            total_draw_counts[card.name] += 1

    for card_name, draw_count in total_draw_counts.items():
        draw_count_percent = round((draw_count / (loops * 7)) * 100, 2)
        print(f"{card_name}: {draw_count_percent}%")
