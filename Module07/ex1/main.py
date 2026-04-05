from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex1.Deck import Deck
from enum import Enum


class Rarity(Enum):
    common = 'Common'
    uncommon = 'Uncommon'
    rare = 'Rare'
    legendary = 'Legendary'


try:
    deck = Deck()
    spell = SpellCard('Lightning Bolt', 3, Rarity.rare.value, 'damage')
    artifact = ArtifactCard('Mana Crystal', 2, Rarity.uncommon.value, 3,
                            '+1 mana per turn')
    creature = CreatureCard('Fire Dragon', 5, Rarity.legendary.value, 12, 95)
    deck.add_card(creature)
    deck.add_card(artifact)
    deck.add_card(spell)
    my_mana = 20

    print("=== DataDeck Deck Builder ===\n")

    print("Building deck with different card types...")
    print(f"Deck stats: {deck.get_deck_stats()}")

    print()

    print("Drawing and playing cards:\n")
    card = deck.draw_card()
    print("Drew: Lightning Bolt (Spell)")

    print(f"Play result: "
          f"{card.play({'card_played': card.name, 'mana': my_mana})}")

    print()

    print("Drew: Mana Crystal (Artifact)")
    card = deck.draw_card()

    print(f"Play result: "
          f"{card.play({'card_played': card.name, 'mana': my_mana})}")

    print()

    print("Drew: Fire Dragon (Creature)")
    card = deck.draw_card()

    print(f"Play result: "
          f"{card.play({'card_played': card.name,  'mana': my_mana})}")

    print()

    print("Polymorphism in action: Same interface, different card behaviors!")
except KeyError as e:
    print(f"\nError: {e}\n")
except ValueError as e:
    print(f"\nError: {e}\n")
