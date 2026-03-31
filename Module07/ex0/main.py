from abc import ABC, abstractmethod
from enum import Enum
from typing import Dict, Any, List
from ex0.CreatureCard import CreatureCard

print("=== DataDeck Card Foundation ===\n")

print("Testing Abstract Base Class Design:\n")

print("CreatureCard Info:")
card = CreatureCard('Fire Dragon', 5, 'Legendary', 7, 5)
print(card.get_card_info())
print()

print("Playing Fire Dragon with 6 mana available:")
print(f"Playable: {card.is_playable(6)}")


print(f"Play result: {card.play({'card_played': card.name})}\n")

print("Fire Dragon attacks Goblin Warrior:")

target = 'Goblin Warrior'
print(f"Attack result: {card.attack_target(target)}\n")

print("Testing insufficient mana (3 available):")

print(f"Playable: {card.is_playable(3)}\n")

print("Abstract pattern successfully demonstrated!")

