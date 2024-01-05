# abilities.py
class Ability:
    def execute(self, game_state, *args, **kwargs):
        pass

class DrawCardAbility(Ability):
    def execute(self, game_state, **kwargs):
        
        if 'draw_count' in kwargs:
            draw_count = kwargs.get('draw_count')
        if 'player_hand' in kwargs:
            player_hand = kwargs.get('player_hand')

        #Logic for the ability 
        print(f"{game_state['player']} draws {draw_count} card from the library.")
        player_hand.add(draw_count)
        print(player_hand.player_hand)

class AddManaAbility(Ability):
    def execute(self, game_state, player_mana_pool, *args, **kwargs):
        
        if 'color' in kwargs:
            color = kwargs.get('color')
        if 'mana_amount' in kwargs:
            mana_amount = kwargs.get('mana_amount')
        
        #Logic for the ability
        print(f"{game_state['player']} gains {mana_amount} {color} mana.")
        player_mana_pool.add_mana(color, mana_amount)
        print(player_mana_pool.mana)

class AddLifeAbility(Ability):
    def execute(self, game_state, *args, **kwargs):
        
        if 'life_amount' in kwargs:
            life_amount = kwargs.get('life_amount')
        if 'player_life' in kwargs:
            player_life = kwargs.get('player_life')
        
        #Logic for the ability
        player_life.gain_life(game_state, life_amount)