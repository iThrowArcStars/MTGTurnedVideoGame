# mana.py
#This file defines how mana should work

class ManaPool:
    def __init__(self):
        self.mana = {}

    def add_mana(self, color, amount):
        self.mana[color] = self.mana.get(color, 0) + amount

    def get_total_mana(self):
        return sum(self.mana.values())
