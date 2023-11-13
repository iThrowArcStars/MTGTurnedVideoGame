#scorcery_card.py
#Scorcery Card Database:
class SorceryCard:
    def __init__(self, name, abilities=None, mana_cost=None, draw_count=0):
        self.name = name
        self.card_type = "Scorcery"
        self.abilities = abilities if abilities else []
        self.mana_cost = mana_cost if mana_cost else []
        self.draw_count = draw_count

#Sorcery Cards:
anger_of_the_gods = SorceryCard(
    name="Anger of the Gods",
    abilities=["Anger of the Gods deals 3 damage to each creature.\n"
            "If a creature dealt damage this way would die this turn,"
            " exile it instead."],
)
escape_the_wild = SorceryCard(
    name="Escape the Wild",
    abilities=["Exile the top five cards of your library."
            "\nYou may play cards exiled this way until the end of your next turn."
            "\n \nYou may play an additional land this turn."],
)
miming_slime = SorceryCard(
    name="Miming Slime",
    abilities=["Put an X/X green Ooze creature token onto the battlefield, where X is the greatest power among creatures you control."],
)
rangers_path = SorceryCard(
    name="Ranger's Path",
    abilities=["Search library for up to two Forest cards and "
            "put them onto \nthe battlefield tapped. Then shuffle your library."],
)
retrieve = SorceryCard(
    name="Retrieve",
    abilities=["Return up to one target creature card and up to one target noncreature permanent card from your graveyard to your hand. Exile Retrieve."],
)