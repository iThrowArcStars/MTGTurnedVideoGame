# dragon_deck.py

from basic_land_card import forest, mountain
from creature_card import (
    atarka_world_render,
    archwing_dragon,
    balefire_dragon,
    elvish_mystic,
    karametras_acolyte,
    llanowar_elves,
    ryusei_the_falling_star,
    slumbering_dragon,
    stormbreath_dragon,
    storm_herald,
    thunderbreak_regent,
    tyrant_of_kher_ridges,
    utvara_hellkite,

    test_creature1,
    test_creature2,
    test_creature3,
    test_creature4,
    test_creature5,
    test_creature6,
    test_creature7
)
from instant_card import (
    defend_the_hearth,
    infuriate,
    lightning_bolt,
    seething_song,
    street_spasm,
)
from enchantment_card import (
    curse_of_bloodletting,
    crucible_of_fire,
    dragon_mantle,
)
from scorcery_card import anger_of_the_gods, escape_the_wild, rangers_path

# Combine all cards into a single list
dragon_deck = [
    *([forest] * 6),
    *([mountain] * 10),
    *([atarka_world_render] * 2),
    *([archwing_dragon] * 2),
    *([balefire_dragon] * 1),
    *([elvish_mystic] * 2),
    *([karametras_acolyte] * 1),
    *([llanowar_elves] * 2),
    *([ryusei_the_falling_star] * 1),
    *([slumbering_dragon] * 3),
    *([stormbreath_dragon] * 2),
    *([storm_herald] * 1),
    *([thunderbreak_regent] * 1),
    *([tyrant_of_kher_ridges] * 1),
    *([utvara_hellkite] * 2),
    *([defend_the_hearth] * 1),
    *([infuriate] * 1),
    *([lightning_bolt] * 3),
    *([seething_song] * 1),
    *([street_spasm] * 1),
    *([curse_of_bloodletting] * 1),
    *([crucible_of_fire] * 1),
    *([dragon_mantle] * 3),
    *([anger_of_the_gods] * 1),
    *([escape_the_wild] * 1),
    *([rangers_path] * 2),
]

test_deck = [
    test_creature1,
    test_creature2,
    test_creature3,
    test_creature4,
    test_creature5,
    test_creature6,
    test_creature7
]
