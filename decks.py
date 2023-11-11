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
    *([mountain] * 6),
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
    defend_the_hearth,
    infuriate,
    lightning_bolt,
    seething_song,
    street_spasm,
    curse_of_bloodletting,
    crucible_of_fire,
    dragon_mantle,
    anger_of_the_gods,
    escape_the_wild,
    rangers_path,
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
