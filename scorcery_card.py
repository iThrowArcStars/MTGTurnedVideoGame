#scorcery_card.py
#Scorcery Card Database:
class ScorceryCard:
    def __init__(self, name, abilities=None, mana_cost=None):
        self.name = name
        self.card_type = "Scorcery"
        self.abilities = abilities if abilities else []
        self.mana_cost = mana_cost if mana_cost else []

#Scorcery Cards:
anger_of_the_gods = ScorceryCard(
    name="Anger of the Gods",
    abilities=["Anger of the Gods deals 3 damage to each creature.\n"
            "If a creature dealt damage this way would die this turn,"
            " exile it instead."]
)
escape_the_wild = ScorceryCard(
    name="Escape the Wild",
    abilities=["Exile the top five cards of your library."
            "\nYou may play cards exiled this way until the end of your next turn."
            "\n \nYou may play an additional land this turn."]
)
rangers_path = ScorceryCard(
    name="Ranger's Path",
    abilities=["Search library for up to two Forest cards and "
            "put them onto \nthe battlefield tapped. Then shuffle your library."]
)