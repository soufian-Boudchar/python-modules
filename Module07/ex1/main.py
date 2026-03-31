from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex1.Deck import Deck


deck = Deck()
spell = SpellCard('Lightning Bolt', 3, 'Rare', 'damage')
artifact = ArtifactCard('Mana Crystal', 2, 'Epic', 3, '+1 mana per turn')
creature = CreatureCard('Fire Dragon', 5, 'legendary', 12, 95)
deck.add_card(creature)
deck.add_card(artifact)
deck.add_card(spell)

print("=== DataDeck Deck Builder ===\n")

print("Building deck with different card types...")
print(f"Deck stats: {deck.get_deck_stats()}")

print()

print(f"Drawing and playing cards:\n")
drawn_card = deck.draw_card()
print("Drew: Lightning Bolt (Spell)")
print(f"Play result: {drawn_card.play({'card_played': drawn_card.name})}")

print()

print("Drew: Mana Crystal (Artifact)")
drawn_card = deck.draw_card()
print(f"Play result: {drawn_card.play({'card_played': drawn_card.name})}")

print()

print("Drew: Fire Dragon (Creature)")
drawn_card = deck.draw_card()
print(f"Play result: {drawn_card.play({'card_played': drawn_card.name})}")

print()

print("Polymorphism in action: Same interface, different card behaviors!")