from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
import random
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard

class Deck:
    def __init__(self):
        self.cards_deck = []
    def add_card(self, card: Card) -> None:
        self.cards_deck.append(card)
    
    def remove_card(self, card_name: str) -> bool:
        for card in self.cards_deck:
            if card.name == card_name:
                self.cards_deck.remove(card)
                return True
        return False
    
    def shuffle(self) -> None:
        random.shuffle(self.cards_deck)
    
    def draw_card(self) -> Card:
        if not self.cards_deck:
            raise ValueError("Deck of cards is empty!")
        return self.cards_deck.pop()

    def get_deck_stats(self) -> dict:
        total_cards = len(self.cards_deck)
        
        creatures = 0
        spells = 0
        artifacts = 0
        _sum_ = 0
        for card in self.cards_deck:
            _sum_ += card.cost
            if isinstance(card, ArtifactCard):
                artifacts += 1
            elif isinstance(card, SpellCard):
                spells += 1
            elif isinstance(card, CreatureCard):
                creatures += 1

        if total_cards > 0:
            avg_cost = _sum_ / total_cards
        else:
            avg_cost = 0.0
        return {
            'total_cards': total_cards,
            'creatures': creatures,
            'spells': spells,
            'artifacts': artifacts,
            'avg_cost': f"{avg_cost:.2f}"
        }