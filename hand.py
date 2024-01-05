# hand.py
import random

class PlayerHand:
    def __init__(self, player_hand=None):
        self.player_hand = player_hand if player_hand is not None else []

    def __len__(self):
        return len(self.player_hand)

    def add(self, draw_count):
        if len(self.player_hand):  # Use len() to check if the hand is not empty
            for _ in range(draw_count):
                if len(self.player_hand) == 0:
                    break
                new_card = random.choice(self.player_hand)
                self.player_hand.remove(new_card)
        else:
            print("The hand is empty. Cannot add a card to the hand.")
            return None
