#Does not work???
import textwrap
from decks import wolf_deck
from decks import dragon_deck
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
