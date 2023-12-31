#card.py
#This file defines what a card is in MTG
class Card:
    def __init__(self, card_name, owner = None, controller = None):
        self.card_name = card_name
        self.owner = owner
        self.controller = controller

