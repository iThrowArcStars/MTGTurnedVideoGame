#hand.py 
#This file initializes a class desribing a player's hand

import random

class PlayerHand:
    def __init__(self, player_hand=None):
        self.player_hand = player_hand if player_hand is not None else []

    def add(self, deck, draw_count):
        if deck:
            for _ in range(draw_count):
                if deck == []:
                    break
                new_card = random.choice(deck)
                self.player_hand.append(new_card)
                deck.remove(new_card)
        else:
            print("The deck is empty. Cannot add a card to the hand.")
            return None  # Return None if the deck is empty