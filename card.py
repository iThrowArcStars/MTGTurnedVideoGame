#card.py
#This file defines what a card is in MTG
class Card:
    def __init__(self, card_name, owner = None, controller = None):
        self.card_name = card_name
        self.owner = owner
        self.controller = controller
    
    def add_ability(self, ability):
        self.abilities.append(ability)

    def apply_abilities(self, game_state):
        for ability in self.abilities:
            ability.execute(game_state)
