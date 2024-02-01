# The deck needs to be in a pre determined order before the start of the game so the player can scry

import random

class Deck:
    def __init__(self, *player_cards):
        self.player_cards = [player_cards]
    
    def shuffle(self):
        random.shuffle(self.player_cards)

    def put_at_bottom(self, card):
        for index, element in enumerate(self.player_cards):
            if card == element:
                removed_card = self.player_cards[index]
                self.player_cards.pop(index)
                self.player_cards.append(removed_card)
    