import random
from all_cards import all_cards 

def draw_seven_cards():
    shuffled_deck = random.sample(all_cards, len(all_cards))

    hand = shuffled_deck[:7]

    return hand

if __name__ == "__main__":
    drawn_cards = draw_seven_cards()

    print("Drawn Cards:")
    for card in drawn_cards:
        print(card.name)
