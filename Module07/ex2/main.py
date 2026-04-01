from ex2.EliteCard import EliteCard
from enum import Enum


class Rarity(Enum):
    common = 'Common'
    uncommon = 'Uncommon'
    rare = 'Rare'
    legendary = 'Legendary'

print("=== DataDeck Ability System ===\n")


print("EliteCard capabilities:")
print("- Card: ['play', 'get_card_info', 'is_playable']")
print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']\n")

print("Playing Arcane Warrior (Elite Card):\n")
try:
    elit_card = EliteCard('Arcane Warrior', 4, Rarity.legendary.value, 5, 'melee', 100, 3)


    print("Combat phase:")
    print(f"Attack result: {elit_card.attack('Enemyy')}")
    print(f"Defense result: {elit_card.defend(5)}")

    print("\nMagic phase:")

    print(f"Spell cast: {elit_card.cast_spell('Fireball', ['Enemy1', 'Enemy2'])}")
    print(f"Mana channel: {elit_card.channel_mana(3)}")

    print()
    
    print("Multiple interface implementation successful!")
except ValueError as e:
    print(f"Error: {e}")
except KeyError as e:
    print(f"Error: {e}")