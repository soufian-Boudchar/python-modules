from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, durability: int, effect: str):
        if not isinstance(effect, str):
            raise ValueError("effect must be string.")
        if not isinstance(durability, int) or durability < 0:
            raise ValueError("durability must be a positive integer.")

        self.effect = effect
        self.durability = durability
        super().__init__(name, cost, rarity)
        
    def play(self, game_state: dict) -> dict:
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': f'permanent: {self.effect}'
        }
    
    def activate_ability(self) -> dict:
        if self.durability > 0:
            self.durability -= 1
            status = "Activated"
        else:
            status = "Destroyed (0 durability)"
        return{
            'action': self.effect,
            'remaining_durability': self.durability,
            'status': status
        }