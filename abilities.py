#abilities.py
#This file defines the abilities on some cards

class Ability:
    def execute(self, game_state):
        pass

class DrawCardAbility(Ability):
    def execute(self, game_state):
        print(f"{game_state['player']} draws a card.")
