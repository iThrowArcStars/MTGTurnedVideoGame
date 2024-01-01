# creature.py
#This file defines all Cards that are considered the subclass Creature
from card import Card

class Creature:
    def __init__(self, name, power, toughness, abilities=None, mana_cost=None):
        self.name = name
        self.power = power
        self.toughness = toughness
        self.abilities = abilities if abilities is not None else self.default_abilities()
        self.mana_cost = mana_cost if mana_cost is not None else {}

    def default_abilities(self):
        # Define default abilities for creatures here
        return []

    def add_ability(self, ability):
        self.abilities.append(ability)

    def perform_abilities(self, game_state, deck, draw_count):
        for ability in self.abilities:
            ability.execute(game_state, deck, draw_count)
