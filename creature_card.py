#creature_card.py
#The Creature Database:
#Creature Types:
DRAGON = "Dragon"
ELF = "Elf"
HUMAN = "Human"
WEREWOLF = "Werewolf"
WOLF = "Wolf"

class CreatureCard:
    def __init__(self, creature_type, name, draw_count, power, toughness, abilities=None, mana_cost=None):
        self.name = name
        self.card_type = "Creature"
        self.creature_type = creature_type  # Use the provided creature_type parameter
        self.abilities = abilities if abilities else []
        self.mana_cost = mana_cost if mana_cost else []
        self.power = power
        self.toughness = toughness
        self.draw_count = draw_count

#Creature Cards:
atarka_world_render = CreatureCard(
    creature_type=DRAGON,
    name="Atarka, World Render",
    power=6,
    toughness=4,
    abilities=["Flying, trample \nWhenever a Dragon you control attacks,"
            "it gains double strike until end of turn. "],
    draw_count=0
)
archwing_dragon = CreatureCard(
    creature_type=DRAGON,
    name="Archwing Dragon",
    power=4,
    toughness=4,
    abilities=["Flying, haste \nAt the beggining of the end step, return Archwing"
            " Dragon to its owner's hand."],
    draw_count=0
)
balefire_dragon = CreatureCard(
    creature_type=DRAGON,
    name="Balefire Dragon",
    power=6,
    toughness=6,
    abilities=["Flying\nWhenever Balefire Dragon daels combat damage to a player"
            ", it deals that much damage to each creature that player controls. "],
    draw_count=0
)
child_of_the_pack = CreatureCard(
    creature_type=HUMAN,
    name="Child of the Pack",
    power=2,
    toughness=5,
    abilities=["UncoloredX2, ChaosX1, ForestX1: Create a 2/2 green Wolf creature token. "
               "\nDaybound (If a player casts no spells during their own turn, it becomes night next turn.)"],
    draw_count=0
)
dragon_whelp = CreatureCard(
    creature_type=DRAGON,
    name="Dragon Whelp",
    power=2,
    toughness=3,
    abilities=["Flying\nChaosX1: +1/0; if more than three mana was spent this"
    "way, Dragon Whelp is destroyed at the end of turn."],
    draw_count=0
)
elvish_mystic = CreatureCard(
    creature_type=ELF,
    name="Elvish Mystic",
    power=1,
    toughness=1,
    abilities=["Tap: Add one Forest to your mana pool."],
    draw_count=0
)
karametras_acolyte = CreatureCard(
    creature_type=HUMAN,
    name="Karametra's Acolyte",
    power=1,
    toughness=4,
    abilities=["Tap: Add an amount of Forest to your mana pool equal to your"
    " devotion to green."],
    draw_count=0
)
llanowar_elves = CreatureCard(
    creature_type=ELF,
    name="Llanowar Elves",
    power=1,
    toughness=1,
    abilities=["Tap: Add one Forest to your mana pool."],
    draw_count=0
)
ryusei_the_falling_star = CreatureCard(
    creature_type=DRAGON,
    name="Ryusei, the Falling Star",
    power=5,
    toughness=5,
    abilities=["Flying\nWhen Ryusei, the Falling Star is put into a graveyard from"
            " play, it deals 5 damage to each creature without flying. "],
    draw_count=0
)
savage_packmate = CreatureCard(
    creature_type=WEREWOLF,
    name="Savage Packmate",
    power=5,
    toughness=5,
    abilities=["Trample"
               "\nOther creatures you control get +1/+0. "
               "\nNightbound (If a player casts at least two spells during their own turn, it becomes day next turn.) "],
    draw_count=0
)
slumbering_dragon = CreatureCard(
    creature_type=DRAGON,
    name="Slumbering Dragon",
    power=3,
    toughness=3,
    abilities=["Flying", "Slumbering Dragon can't attack or block unless"
    "it has five or more +1/+1 counters on it. Whenever a creature attacks you"
    "or a planeswalker you control, put a +1/+1 counter on Slumbering Dragon."],
    draw_count=0
)
snarling_wolf = CreatureCard(
    creature_tpye=WOLF,
    name="Snarling Wolf",
    power=1,
    toughness=1,
    abilities=["UncoloredX1, ForestX1: Snarling Wolf gets +2/+2 until end of turn. Activate only once each turn. "],
    draw_count=0
)
stormbreath_dragon = CreatureCard(
    creature_type=DRAGON,
    name="Stormbreath Dragon",
    power=4,
    toughness=4,
    abilities=["Flying, haste, prtection from white"
            "\nUncoloredX5 and ChaosX2: Monstrosity 3."
            "\n\nWhen Stormbreath Dragon becomes monstrous, it deals damage to"
            "each opponent equal to the number of cards in that player's hand."],
    draw_count=0
)
storm_herald = CreatureCard(
    creature_type=HUMAN,
    name="Storm Herald",
    power=3,
    toughness=2,
    abilities=["Haste\nWhen Storm Herald enter the battlefield, return any number"
            "of Aura cards from your graveyard to the battlefield attached"
            " to creatures you control. Exile all those Auras at the begining of"
            " your next end step. If those Auras would leave the battlefield,"
            " exile them instead of putting them anywhere else. "],
    draw_count=0
)
thunderbreak_regent = CreatureCard(
    creature_type=DRAGON,
    name="Thunderbreak Regent",
    power=4,
    toughness=4,
    abilities=["Flying\nWhenever a Dragon you control becomes the target of a"
    " spell or ability an opponent controls, Thunderbreak Regent"
    " deals 3 damage to that player."],
    draw_count=0
)
tyrant_of_kher_ridges = CreatureCard(
    creature_type=DRAGON,
    name="Tyrant of Kher Ridges",
    power=4,
    toughness=5,
    abilities=["Flying\nWhen Tyrant of Kher Ridges enters the battlefield, it"
            " deals 4 damage to any target. "
            "\nChaosX1: Tyrant of Kher Ridges gets +1/+0 until the end of turn"],
    draw_count=0
)
utvara_hellkite = CreatureCard(
    creature_type=DRAGON,
    name="Utvara Hellkite",
    power=6,
    toughness=6,
    abilities=[ "Flying\nWhenever a Dragon you control attacks, put a 6/6 "
    "red Dragon creature token with flying into the battlefield. "],
    draw_count=0
)
utvara_corgi = CreatureCard(
    creature_type=WOLF,
    name="Utvara Corgi",
    power=2,
    toughness=2,
    abilities=[ "Deathtouch, infect\nWhenever another creature attacks, put a 1/1 "
    "Green wolf creature token with infect into the battlefield. "],
    draw_count=0
)


#test class and creature

class TestCard:
    def __init__(self, name, power, toughness, draw_count):
        self.name = name
        self.power = power
        self.toughness = toughness
        self.draw_count = draw_count


test_creature1 = TestCard(
    name="Test Creature",
    power=999,
    toughness=999,
    draw_count = 0
)
test_creature2 = TestCard(
    name="Test Creature",
    power=999,
    toughness=999,
    draw_count = 0
)
test_creature3 = TestCard(
    name="Test Creature",
    power=999,
    toughness=999,
    draw_count = 0
)
test_creature4 = TestCard(
    name="Test Creature",
    power=999,
    toughness=999,
    draw_count = 0
)
test_creature5 = TestCard(
    name="Test Creature",
    power=999,
    toughness=999,
    draw_count = 0
)
test_creature6 = TestCard(
    name="Test Creature",
    power=999,
    toughness=999,
    draw_count = 0
)
test_creature7 = TestCard(
    name="Test Creature",
    power=999,
    toughness=999,
    draw_count = 0
)