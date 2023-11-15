#enchantment_card.py
#Enchantment Card Database:
class EnchantmentCard:
    def __init__(self, name, abilities=None, mana_cost=None, draw_count=0,):
        self.name = name
        self.card_type = "Enchantment"
        self.abilities = abilities if abilities else []
        self.mana_cost = mana_cost if mana_cost else []
        self.draw_count = draw_count

#Enchantment Cards:
audacity = EnchantmentCard(
    name="Audacity",
    abilities=["Enchant creature"
               "\nEnchanted creature gets +2/+0 and has trample. "
               "\nWhen Audacity is put into a graveyard from the battlefield, draw card. "],
)
blanchwood_armor = EnchantmentCard(
    name="Blanchwood Armor",
    abilities=["Enchant creature"
               "\nEnchanted creature get +1/+1 for each Forest you control. "],
)
curse_of_bloodletting = EnchantmentCard(
    name="Curse of Bloodletting",
    abilities=["Enchant player"
            "\nIf a sorce would deal damage to enchanted player, it deals double that damage to that player instead. "],
)
crucible_of_fire = EnchantmentCard(
    name="Crucible of Fire",
    abilities=["Dragon creatures you control get +3/+3."],
)
dragon_mantle = EnchantmentCard(
    name="Dragon Mantle",
    abilities=["Enchant creature"
               "\nWhen Dragon Mantle enters the battlefield, draw a card."
               "\nEnchanted creature has 'ChaosX1: This creature gets +1/+0 until end of turn.'"],
)
glorious_sunrise = EnchantmentCard(
    name="Glorious Sunrise",
    abilities=["At the beginning of combat on your turn, choose one"
               "\nCreatures you control get +1/+1 and gain trample until the end of turn. "
               "\nTarget land gains 'Tap: Add ForestX3' until end of turn. "
               "\nDraw card if you control a creature with 3 or more power. "
               "\nYou gain 3 life. "],
)
wild_defiance = EnchantmentCard(
    name="Wild Defiance",
    abilities=["Whenever a creature you control becomes the target of an instant or scorcery spell, that creature gets +3/+3 until end of turn. "],
)