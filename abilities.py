#abilities.py
#This file defines the abilities on some cards

from hand import PlayerHand

class Ability:
    def execute(self):
        pass

class DrawCard(Ability):
    def execute(self, player_hand, deck):
        print(f"Player draws a card.")
        player_hand.add(deck)

