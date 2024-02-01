# game.py

from mana import ManaPool
from hand import PlayerHand
from life import Life
from abilities import DrawCardAbility, AddManaAbility, AddLifeAbility
from decks import Deck


from card import Creature, Enchantment, Instant

draw_card_ability = DrawCardAbility()
add_mana_ability = AddManaAbility()
add_life_ability = AddLifeAbility()
player_one_hand = PlayerHand()

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
player_one_deck = Deck(
    test_creature,
    test_enchantment,
    test_instant
)


game_status = True 
if game_status == True:
    player_one_deck.shuffle()
    print(player_one_deck.player_cards)
    player_one_hand.add(7)
    print(player_one_hand.player_hand)
