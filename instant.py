#instant.py
#This file defines all Cards that are considered part of the subclass Instant
from card import Card
class Instant(Card):
    def __init__(self, card_name, abilities=None, mana_cost=None):
        super().__init__(card_name)
        self.abilities = abilities
        self.mana_cost = mana_cost
