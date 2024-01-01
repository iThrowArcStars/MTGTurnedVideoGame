#abilities.py
#This file defines the abilities on some cards

class Ability:
    def execute(self, game_state):
        pass

class DrawCard(Ability):
    def execute(self, game_state, deck, draw_count):
        print(f"{game_state['player']} draws {draw_count} card from the library.")