from ex0.Card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, attack: int, health: int):
        if not isinstance(attack, int) or not isinstance(health, int):
            raise ValueError("Attack and health must be positive integers.")
        if attack < 0 or health < 0:
            raise ValueError("Attack and health must be positive integers.")

        self.attack = attack
        self.health = health


        super().__init__(name, cost, rarity)



    def play(self, game_state: dict) -> dict:
        return {
            'card_played': game_state['card_played'],
            'mana_used': game_state['mana_used'],
            'effect': game_state['effect']
        }
    def attack_target(self, target) -> dict:
        target_name = target if isinstance(target, str) else target.name
        return {
            'attacker': self.name,
            'target': target_name,
            'damage_dealt': self.attack,
            'combat_resolved': True
        }