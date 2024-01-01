# main.py
from mana import ManaPool
from battlefield import Battlefield
from hand import PlayerHand
from abilities import Ability, DrawCard

from creature import Creature

draw_card_ability = DrawCard()

test_creature = Creature(
    name="Test Creature",
    power=5,
    toughness=4,
    mana_cost={"Red": 2, "Colorless": 3},
    abilities=[draw_card_ability]
)

# Simulate performing abilities during the game
deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
game_state = {'player': 'Player 1'}
battlefield = Battlefield()
p1_mana_pool = ManaPool()
p1_hand = PlayerHand()

p1_mana_pool.add_mana("Red", 4)
p1_mana_pool.add_mana("Colorless", 3)
print(p1_mana_pool.mana)
battlefield.add(test_creature, p1_mana_pool)
draw_count = 2
test_creature.perform_abilities(game_state, deck, draw_count)