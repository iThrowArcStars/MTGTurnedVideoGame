# card.py

class Card:
    def __init__(self, name, mana_cost=None):
        self.name = name
        self.mana_cost = mana_cost if mana_cost else []