#enchantment_card.py
#Enchantment Card Database:
class EnchantmentCard:
    def __init__(self, name, draw_count, abilities=None, mana_cost=None):
        self.name = name
        self.card_type = "Enchantment"
        self.abilities = abilities if abilities else []
        self.mana_cost = mana_cost if mana_cost else []
        self.draw_count = draw_count

#Enchantment Cards:
curse_of_bloodletting = EnchantmentCard(
    name="Curse of Bloodletting",
    abilities=["Enchant player"
            "\nIf a sorce would deal damage to enchanted player, it deals double"
            " that damage to that player instead. "],
    draw_count=0
)
crucible_of_fire = EnchantmentCard(
    name="Crucible of Fire",
    abilities=["Dragon creatures you control get +3/+3."],
    draw_count=0
)
dragon_mantle = EnchantmentCard(
    name="Dragon Mantle",
    abilities=["Enchant creature\nWhen Dragon Mantle"
            " enters the battlefield, draw a card.\nEnchanted creature has 'Chaos"
            "X1: This creature gets +1/+0 until end of turn.'"],
    draw_count=0
)