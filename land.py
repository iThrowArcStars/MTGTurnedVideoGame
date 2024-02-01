from card import Card
class Land(Card):
    def __init__(self, istapped, abilities=None):
        self.abilities = abilities
        self.istapped = istapped

    def tap_land(self):
        self.istapped = True
