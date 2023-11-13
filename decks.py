# dragon_deck.py

from basic_land_card import forest, mountain
from creature_card import (
    atarka_world_render,
    archwing_dragon,
    balefire_dragon,
    child_of_the_pack,
    elvish_mystic,
    karametras_acolyte,
    llanowar_elves,
    ryusei_the_falling_star,
    savage_packmate,
    slumbering_dragon,
    snarling_wolf,
    stormbreath_dragon,
    storm_herald,
    thunderbreak_regent,
    tyrant_of_kher_ridges,
    utvara_hellkite,

)
from instant_card import (
    defend_the_hearth,
    echoing_courage,
    infuriate,
    lightning_bolt,
    massive_might,
    seething_song,
    street_spasm,
    witchs_web
)
from enchantment_card import (
    audacity,
    blanchwood_armor,
    curse_of_bloodletting,
    crucible_of_fire,
    dragon_mantle,
    glorious_sunrise,
    wild_defiance
)
from scorcery_card import (
    anger_of_the_gods, 
    escape_the_wild,
    miming_slime, 
    rangers_path,
    retrieve
)
# Combine all cards into a single list
dragon_deck = [
    #Lands
    *([forest] * 6),
    *([mountain] * 10),
    #Creatures
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
    #Instants
    *([defend_the_hearth] * 1),
    *([infuriate] * 1),
    *([lightning_bolt] * 3),
    *([seething_song] * 1),
    *([street_spasm] * 1),
    #Enchantments
    *([curse_of_bloodletting] * 1),
    *([crucible_of_fire] * 1),
    *([dragon_mantle] * 3),
    #Scorcery
    *([anger_of_the_gods] * 1),
    *([escape_the_wild] * 1),
    *([rangers_path] * 2),
]

wolf_deck = [
    # Lands
    *([forest] * 21),
    *([mountain] * 4),
    # Creatures
    *([child_of_the_pack] * 1),
    *([snarling_wolf] * 1),
    *([savage_packmate] * 0),
    # Instants
    *([echoing_courage] * 1),
    *([massive_might] * 1),
    *([witchs_web] * 2),
    # Enchantments
    *([audacity] * 1),
    *([blanchwood_armor] * 1),
    *([glorious_sunrise] * 1),
    *([wild_defiance] * 1),
    # Sorcery
    *([miming_slime] * 2),
    *([retrieve] * 1)
]
