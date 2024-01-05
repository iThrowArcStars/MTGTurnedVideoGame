# main.py
from mana import ManaPool
from battlefield import Battlefield
from life import Life
from hand import PlayerHand
from abilities import Ability, DrawCard, AddMana

from creature import Creature

draw_card_ability = DrawCard()
add_mana_ability = AddMana()

test_creature01 = Creature(
    name="Test Creature01",
    power=5,
    toughness=4,
    mana_cost={"Red": 2, "Colorless": 3},
    abilities=[draw_card_ability]
)
test_creature02 = Creature(
    name="Test Creature02",
    power=5,
    toughness=4,
    mana_cost={"Red": 2, "Colorless": 3},
    abilities=[add_mana_ability]
)

# Simulate performing abilities during the game
deck = [test_creature01, test_creature02]
game_state = {'player': 'Player 1'}
battlefield = Battlefield()
p1_mana_pool = ManaPool()
p1_hand = PlayerHand()
p1_life = Life()

p1_life.gain_life(game_state, 4)

p1_hand.add(deck, 7)

p1_mana_pool.add_mana("Red", 4)
p1_mana_pool.add_mana("Colorless", 3)
print(p1_mana_pool.mana)
battlefield.add(game_state, test_creature01, p1_mana_pool)
amount = 7
test_creature02.perform_abilities(game_state, p1_mana_pool, "Red", amount)