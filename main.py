# main.py
from mana import ManaPool
from battlefield import Battlefield
from hand import PlayerHand
from abilities import Ability, DrawCard

from creature import test_creature_card
from instant import test_instant_card_1, test_instant_card_2

deck = [1,2,3,4,5,6,7,8,9,10]
battlefield = Battlefield()
p1_hand = PlayerHand([])
draw_card_ability = DrawCard()
draw_card_ability.execute(p1_hand, deck)

print(p1_hand)