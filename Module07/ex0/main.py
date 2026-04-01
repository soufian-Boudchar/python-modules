from abc import ABC, abstractmethod
from enum import Enum
from typing import Dict, Any, List
from ex0.CreatureCard import CreatureCard

class Rarity(Enum):
    common = 'Common'
    uncommon = 'Uncommon'
    rare = 'Rare'
    legendary = 'Legendary'
    
print("=== DataDeck Card Foundation ===\n")

print("Testing Abstract Base Class Design:\n")

print("CreatureCard Info:")
card = CreatureCard('Fire Dragon', 5, Rarity.rare.value, 7, 5)
my_mana = 6
print(card.get_card_info())
print()

print("Playing Fire Dragon with 6 mana available:")
print(f"Playable: {card.is_playable(6)}")

try:
    print(f"Play result: {card.play({'card_played': card.name, 'mana': my_mana})}\n")



    print("Fire Dragon attacks Goblin Warrior:")

    target = 'Goblin Warrior'
    print(f"Attack result: {card.attack_target(target)}\n")

    print("Testing insufficient mana (3 available):")
    my_mana = 3
    print(f"Playable: {card.is_playable(my_mana)}\n")

    print("Abstract pattern successfully demonstrated!")
except KeyError as e:
    print(f"\nError: {e}\n")
except ValueError as e:
    print(f"\nError: {e}\n")

