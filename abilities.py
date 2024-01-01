#abilities.py
#This file defines the abilities on some cards

import random

from hand import PlayerHand

class Ability:
    def execute(self, game_state):
        pass

class DrawCard(Ability):
    def execute(self, game_state, deck, player_hand, draw_count):
        print(f"{game_state['player']} draws {draw_count} card from the library.")
        player_hand.add(deck, draw_count)
        print(player_hand.player_hand)