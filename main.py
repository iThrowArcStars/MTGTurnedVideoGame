# main.py
from mana import ManaPool
from hand import PlayerHand
from abilities import DrawCardAbility, AddManaAbility

from card import Creature

draw_card_ability = DrawCardAbility()
add_mana_ability = AddManaAbility()

test_creature = Creature(
    name="Test Creature",
    power=5,
    toughness=4,
    mana_cost={"Red": 2, "Colorless": 3},
    abilities=[draw_card_ability, add_mana_ability]
)

# Simulate performing abilities during the game

# Sets basic data required to play game 
game_state = {'player': 'Player 1'}
player_hand = PlayerHand()
player_mana_pool = ManaPool()

draw_count = 2
color = "Red"
amount = 1
test_creature.perform_abilities(game_state, player_mana_pool=player_mana_pool, player_hand=player_hand, draw_count=draw_count, amount=amount, color=color)
