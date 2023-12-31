# main.py
from mana import ManaPool
from battlefield import Battlefield

from creature import test_creature_card
from instant import test_instant_card_1, test_instant_card_2

p1_mana_pool = ManaPool()
battlefield = Battlefield()
battlefield.print_battlefield()
p1_mana_pool.add_mana("Colorless", 5)
print(p1_mana_pool.mana)

# Correct the order of parameters in the add method
battlefield.add(test_creature_card, p1_mana_pool)
battlefield.print_battlefield()