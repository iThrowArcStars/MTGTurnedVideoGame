import textwrap
from all_cards import *

if __name__ == "__main__":
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

# Print card information
print_card_info(atarka_world_render)
print_card_info(archwing_dragon)
print_card_info(lightning_bolt)
print_card_info(street_spasm)
print_card_info(curse_of_bloodletting)