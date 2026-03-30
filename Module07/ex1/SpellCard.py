from ex0.Card import Card


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):


        if not isinstance(effect_type, str):
            raise ValueError("effect_type must be string.")

        self.effect_type = effect_type
        super().__init__(name, cost, rarity)


    def play(self, game_state: dict) -> dict:
        if self.effect_type.lower() == "damage":
            effect_msg = f"Deal {self.cost} damage to target"
        elif self.effect_type.lower() == "heal":
            effect_msg = f"Restore {self.cost} health to target"
        else:
            effect_msg = f"Cast {self.effect_type} spell"
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': effect_msg
        }

    def resolve_effect(self, targets: list) -> dict:
        return {
            'action': self.effect_type,
            'targets': targets,
            'status': 'resolved'
        }
