# card.py
class Card:
    def __init__(self, name, mana_cost=None, abilities=None):
        self.name = name
        self.mana_cost = mana_cost if mana_cost is not None else {}
        self.abilities = abilities if abilities is not None else []

    def add_ability(self, ability):
        self.abilities.append(ability)

class Creature(Card):
    def __init__(self, name, power, toughness, mana_cost=None, abilities=None):
        super().__init__(name, mana_cost, abilities)
        self.power = power
        self.toughness = toughness

    def add_ability(self, ability):
        self.abilities.append(ability)

    def perform_abilities(self, game_state, *args, **kwargs):
        for ability in self.abilities:
            ability.execute(game_state, *args, **kwargs)