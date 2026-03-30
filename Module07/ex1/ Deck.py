from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from random import shuffle
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
        shuffle(self.cards_deck)
    
    def draw_card(self) -> Card:
        if not self.cards_deck:
            raise ValueError("Deck of cards is empty!")
        return self.cards_deck.pop()

    def get_deck_stats(self) -> dict:
        total_cards = len(self.cards_deck)
        
        spells = 0
        creatures = 0
        artifacts = 0
        avg = 0
        for card in self.cards_deck:
            avg += card.cost
            if isinstance(card, ArtifactCard):
                artifacts += 1
            elif isinstance(card, SpellCard):
                spells += 1
            elif isinstance(card, CreatureCard):
                creatures += 1
        
