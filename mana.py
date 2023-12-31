#This file defines how mana should work
class ManaPool:
    def __init__(self):
        self.mana = {"Colorless":0, "Artifact":0, "Red":0, "Green":0, "Black":0, "White":0, "Blue":0} #All the options for mana
    
    def add_mana(self, color, amount):
        self.mana[color] += amount

    def remove_mana(self, color, amount):
        if self.mana[color] >= amount:
            self.mana[color] -= amount
            return True
        return False

mana_pool = ManaPool()
mana_pool.add_mana("Colorless", 5)
print(mana_pool.mana)