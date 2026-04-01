from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str,
                 cost: int,
                 rarity: str,
                 damage: int,
                 combat_type: str,
                 health: int,
                 defense: int):
        if (not isinstance(damage, int) or
            not isinstance(health, int) or
            not isinstance(defense, int)):
            raise ValueError("damage and health and defense must be a positive integer.")
        if not isinstance(combat_type, str):
             raise ValueError("combat_type must be string.")

        self.defense = defense
        self.health = health
        self.damage = damage
        self.combat_type = combat_type
        super().__init__(name, cost, rarity)
    def play(self, game_state: dict) -> dict:
        try:
            if game_state['mana'] < self.cost:
                raise ValueError("Mana is not enough")
        except KeyError:
            raise KeyError("Mana is not found in game_state !")

        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'health': self.health
        }
    def attack(self, target) -> dict:
        return {
            'attacker': self.name,
            'target': target,
            'damage': self.damage,
            'combat_type': self.combat_type
        }

    def defend(self, incoming_damage: int) -> dict:
        taken = incoming_damage - self.defense
        if taken < 0:
            taken = 0
            
            
        health -= taken
        return {
            'defender': self.name,
            'damage_taken': taken,
            'damage_blocked': self.defense,
            'still_alive': self.health > 0
        }
    
    def get_combat_stats(self) -> dict:
        return{
            'damage': self.damage,
            'defense': self.defense,
            'health': self.health,
            'combat_type': self.combat_type
        }
    
    def cast_spell(self, spell_name: str, targets: list) -> dict:
        return {
            'caster': self.name,
            'spell': spell_name,
            'targets': targets,
            'mana_used': self.cost
        }
    
    def channel_mana(self, amount: int) -> dict:
        return {
            'channeled': amount,
            'total_mana': amount + self.cost
        }
    
    def get_magic_stats(self) -> dict:
        return{
            'damage': self.damage,
            'defense': self.defense,
            'health': self.health,
            'combat_type': self.combat_type
        }
