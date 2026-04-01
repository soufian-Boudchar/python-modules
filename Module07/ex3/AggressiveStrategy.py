from ex3.GameStrategy import GameStrategy
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard


class AggressiveStrategy(GameStrategy):

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        cards_played = []
        mana_used = 0
        damage_dealt = 0
        
        available_mana = 5
        
        for card in hand:
            if card.cost <= available_mana:
                cards_played.append(card.name)
                mana_used += card.cost
                available_mana -= card.cost
                
                if isinstance(card, CreatureCard):
                    damage_dealt += card.attack
                elif isinstance(card, SpellCard):
                        damage_dealt += card.cost
        
        return {
            'cards_played': cards_played,
            'mana_used': mana_used,
            'targets_attacked': ["Enemy Player"],
            'damage_dealt': damage_dealt
        }
            
    
    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"
    
    def prioritize_targets(self, available_targets: list) -> list:
        return [available_targets]