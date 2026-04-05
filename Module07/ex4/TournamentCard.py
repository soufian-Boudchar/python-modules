from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):

    def __init__(self, card_id: str, name: str, cost: int, rarity: str,
                 damage: int, defense: int, health: int, initial_rating: int):
        self.card_id = card_id
        self.damage = damage
        self.defense = defense
        self.health = health
        self.wins = 0
        self.losses = 0
        self.rating = initial_rating
        super().__init__(name, cost, rarity)

    def play(self, game_state: dict) -> dict:
        return {'card_played': self.name, 'mana_used': self.cost}

    def attack(self, target) -> dict:
        return {'attacker': self.name, 'target': target, 'damage': self.damage}

    def defend(self, incoming_damage: int) -> dict:
        taken = incoming_damage - self.defense
        if taken < 0:
            taken = 0
        self.health -= taken
        return {
            'defender': self.name,
            'damage_taken': taken,
            'still_alive': self.health > 0
        }

    def get_combat_stats(self) -> dict:
        return {
            'damage': self.damage,
            'defense': self.defense,
            'health': self.health
        }

    def calculate_rating(self) -> int:
        return self.rating

    def update_wins(self, wins: int) -> None:
        self.wins += wins

    def update_losses(self, losses: int) -> None:
        self.losses += losses

    def get_rank_info(self) -> dict:
        return {
            'rating': self.rating,
            'wins': self.wins,
            'losses': self.losses
        }

    def get_tournament_stats(self) -> dict:
        return {
            'interfaces': ['Card', 'Combatable', 'Rankable'],
            'rating': self.rating,
            'record': f"{self.wins}-{self.losses}"
        }
