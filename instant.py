#instant.py
#This file defines all Cards that are considered part of the subclass Instant
from card import Card
class Instant(Card):
    def __init__(self, card_name, abilities=None, mana_cost=None):
        super().__init__(card_name)
        self.abilities = abilities
        self.mana_cost = mana_cost

#All instants:
test_instant_card_1 = Instant("Test Card 1", abilities=["Has a test ability."], mana_cost={"R": 5, "B": 3})
test_instant_card_2 = Instant("Test Card 2", abilities=["Another test ability."], mana_cost={"G": 2, "U": 1})