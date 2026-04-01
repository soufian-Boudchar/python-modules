from ex0.Card import Card
from ex3.CardFactory import CardFactory
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard

class FantasyCardFactory(CardFactory):
    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, int):
            return CreatureCard('dragon', 5, 'rare', name_or_power, 150)
        elif isinstance(name_or_power, str):
            return CreatureCard(name_or_power, 2, 'uncommon', 2, 100)
        else:
            return CreatureCard('goblin', 4, 'uncommon', 2, 100)
    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, int):
            return SpellCard('fireball', 1, 'common', 'damage')
        elif isinstance(name_or_power, str):
            return SpellCard(name_or_power, 1, 'common', 'damage')
        else:
            return SpellCard('fire dragon', 1, 'common', 'damage')

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, int):
            return ArtifactCard('mana_ring', 2, 'uncommon', name_or_power, '+1 mana per turn')
        elif isinstance(name_or_power, str):
            return ArtifactCard(name_or_power, 2, 'uncommon', 6, '+1 mana per turn')
        else:
            return ArtifactCard('health_ring', 2, 'uncommon', 6, '+20 health per turn')

    def create_themed_deck(self, size: int) -> dict:
        return{
            'theme': 'Fantasy',
            'size': size,
            'status': 'Deck created successfully'
        }

    def get_supported_types(self) -> dict:
        return {
            'creatures':  ['dragon', 'goblin'],
            'spells': ['fireball'],
            'artifacts': ['mana_ring']
        }