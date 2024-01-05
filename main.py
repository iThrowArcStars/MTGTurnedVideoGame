# main.py
from mana import ManaPool
from hand import PlayerHand
from life import Life
from abilities import DrawCardAbility, AddManaAbility, AddLifeAbility

from card import Creature, Enchantment, Instant

draw_card_ability = DrawCardAbility()
add_mana_ability = AddManaAbility()
add_life_ability = AddLifeAbility()

test_creature = Creature(
    name="Test Creature",
    power=5,
    toughness=4,
    creature_type = 'Dragon',
    mana_cost={"Red": 2, "Colorless": 3},
    abilities=[draw_card_ability, add_mana_ability, add_life_ability]
)

test_enchantment = Enchantment(
    name="Test Enchantment",
    mana_cost={"Red":1, "Colorless": 3},
    abilities=[draw_card_ability]
)

test_instant = Instant(
    name="Test Instant",
    mana_cost={"Red": 1},
    abilities=[]
)

# Simulate performing abilities during the game

# Sets basic data required to play game 
game_state = {'player': 'Player 1'}
player_hand = PlayerHand()
player_mana_pool = ManaPool()
player_life = Life()

draw_count = 2
color = "Red"
mana_amount = 1
test_creature.perform_abilities(game_state, player_mana_pool=player_mana_pool, player_hand=player_hand, draw_count=draw_count, mana_amount=mana_amount, color=color, life_amount=4, player_life=player_life)
test_enchantment.perform_abilities(game_state, player_hand=player_hand, draw_count=draw_count)
test_instant.perform_abilities(game_state)