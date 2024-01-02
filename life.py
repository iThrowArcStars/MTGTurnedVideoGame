#life.py
#This file describes the behaviors of a player's life

class Life:
    def __init__(self):
        self.player_life = 20

    def add(self, game_state, gained_life):
        print(f"{game_state['player']} gains {gained_life} life.")
        self.player_life += gained_life
        print(self.player_life)