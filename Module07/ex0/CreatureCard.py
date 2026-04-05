from ex0.Card import Card


class CreatureCard(Card):

    def __init__(self, name: str, cost: int, rarity: str, attack: int,
                 health: int):
        if not isinstance(attack, int) or not isinstance(health, int):
            raise ValueError("Attack and health must be positive integers.")
        if attack < 0 or health < 0:
            raise ValueError("Attack and health must be positive integers.")

        self.attack = attack
        self.health = health

        super().__init__(name, cost, rarity)

    def play(self, game_state: dict) -> dict:
        try:
            if not self.is_playable(game_state['mana']):
                raise ValueError("Mana is not enough")
        except KeyError:
            raise KeyError("Mana is not found in game_state!")
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': 'Creature summoned to battlefield'
        }

    def attack_target(self, target) -> dict:
        return {
            'attacker': self.name,
            'target': target,
            'damage_dealt': self.attack,
            'combat_resolved': True
        }
