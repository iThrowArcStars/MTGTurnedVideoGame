#basic_land_card.py
#Basic Land Database:
class BasicLandCard:
    def __init__(self, name, abilities, draw_count):
        self.name = name
        self.card_type = "Basic Land"
        self.abilities = abilities
        self.draw_count = draw_count
  
#Basic Land Cards:
mountain = BasicLandCard(
    name="Mountain",
    abilities=["Tap: Add one Chaos"],
    draw_count=0
)
forest = BasicLandCard(
    name="Forest",
    abilities=["Tap: Add one Forest"],
    draw_count=0
)
plains = BasicLandCard(
    name="Plains",
    abilities=["Tap: Add one Plains"],
    draw_count=0
)
swamp = BasicLandCard(
    name="Swamp",
    abilities=["Tap: Add one Swamp"],
    draw_count=0
)
island = BasicLandCard(
    name="Island",
    abilities=["Tap: Add one Island"],
    draw_count=0
)

class ManaPool:
    def __init__(self):
        pass