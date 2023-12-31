#This file defines all Cards that are considered the subclass Creature
from card import Card
class Creature(Card):
    def __init__(self, power, toughness, abillities = None, mana_cost = None):
        self.abillities = abillities
        self.mana_cost = mana_cost
        self.power = power
        self.toughness = toughness

#Creature Cards:
        