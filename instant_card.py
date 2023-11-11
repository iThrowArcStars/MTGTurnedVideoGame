#instant_card.py
#Instant Card Database:
class InstantCard:
    def __init__(self, name, draw_count, abilities=None, mana_cost=None):
        self.name = name
        self.card_type = "Instant"
        self.abilities = abilities if abilities else []
        self.mana_cost = mana_cost if mana_cost else []
        self.draw_count = draw_count

#Instant Cards:
defend_the_hearth = InstantCard(
    name="Defend the Hearth",
    abilities=["Prevent all combat damage that would be dealt to players this turn."],
    draw_count=0
)
infuriate = InstantCard(
    name="Infuriate",
    abilities=["Target creature gets +3/+2 until the end of turn. "],
    draw_count=0
)
lightning_bolt = InstantCard(
    name="Lightning Bolt",
    abilities=["Lightning Bolt deals 3 damage to target creature or player. "],
    draw_count=0
)
seething_song = InstantCard(
    name="Seething Song",
    abilities=["Add 5 Chaos to your mana pool"],
    draw_count=0
)
street_spasm = InstantCard(
    name="Street Spasm",
    abilities=["Street Spasm deals X damage to target creature without flying"
            "you don't control \n \n Overload: XX 2Chaos \n("
            "You may cast this spell for it's Overload cost. \nIf you do, change"
            " its text by replacing all instances of 'target' with 'each.')"],
    draw_count=0
)