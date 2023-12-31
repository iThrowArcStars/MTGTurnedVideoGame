#This file defines all Cards that are considered the subclass Creature
from card import Card
class Creature(Card):
    def __init__(self, card_name, power, toughness, abillities = None, mana_cost = None):
        super().__init__(card_name)
        self.abillities = abillities
        self.mana_cost = mana_cost
        self.power = power
        self.toughness = toughness

#Creature Cards:
test_creature_card = Creature("Test Creature", 5, 4, "Test ability", {"Red": 2, "Colorless": 3})