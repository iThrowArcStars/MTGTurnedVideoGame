#This file defines how mana should work
class ManaPool:
    def __init__(self):
        self.mana = {"Colorless":0, "Artifact":0, "Red":0, "Green":0, "Black":0, "White":0, "Blue":0}
    
    def add_mana(self, color, amount):
        self.mana[color] += amount

    def remove_mana(self, color, amount):
        if self.mana[color] >= amount:
            self.mana[color] -= amount
            return True
        return False
    
    def get_total_mana(self):
        return sum(self.mana.values())