#abilities.py
#This file defines the abilities on some cards

import random

from hand import PlayerHand

class Ability:
    def execute(self, game_state):
        pass

class DrawCard(Ability):
    def execute(self, game_state: dict, deck: list, player_hand: list, amount: int):
        print(f"{game_state['player']} draws {amount} card from the library.")
        player_hand.add(deck, amount)
        print(player_hand.player_hand)

class AddMana(Ability):
    def execute(self, game_state: dict, player_mana_pool: dict, color: str, amount: int):
        print(f"{game_state['player']} gains {amount} {color} mana.")
        player_mana_pool.add_mana(color, amount)
        print(player_mana_pool.mana)