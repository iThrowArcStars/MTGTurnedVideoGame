#basic_land_card.py
#Basic Land Database:
class BasicLandCard:
    def __init__(self, name, abilities, draw_count=0):
        self.name = name
        self.card_type = "Basic Land"
        self.abilities = abilities
        self.draw_count = draw_count
  
#Basic Land Cards:
mountain = BasicLandCard(
    name="Mountain",
    abilities=["Tap: Add one Chaos"],
)
forest = BasicLandCard(
    name="Forest",
    abilities=["Tap: Add one Forest"],
)
plains = BasicLandCard(
    name="Plains",
    abilities=["Tap: Add one Plains"],
)
swamp = BasicLandCard(
    name="Swamp",
    abilities=["Tap: Add one Swamp"],
)
island = BasicLandCard(
    name="Island",
    abilities=["Tap: Add one Island"],
)

class ManaPool:
    def __init__(self):
        self.mana = {"R": 0, "G": 0, "B": 0, "U": 0, "W": 0, "C": 0}

    def add_mana(self, color, amount):
        self.mana[color] += amount

    def spend_mana(self, color, amount):
        if self.mana[color] >= amount:
            self.mana[color] -= amount
            return True
        return False
