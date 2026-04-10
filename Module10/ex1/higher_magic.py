from typing import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:

    def combiner(target: str, power: int) -> tuple:
        return (spell1(target, power), spell2(target, power))

    return combiner


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:

    def amplifier(target: str, power: int) -> str:
        new_power = power * multiplier
        return base_spell(target, new_power)

    return amplifier


def conditional_caster(condition: Callable, spell: Callable) -> Callable:

    def caster(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"

    return caster


def spell_sequence(spells: list[Callable]) -> Callable:

    def sequence(target: str, power: int) -> list[str]:
        results: list[str] = []
        for spell in spells:
            results.append(spell(target, power))
        return results

    return sequence

def lightning(target: str, power: int):
    return "spell Created !"

def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def fireball(target: str, power):
    return f"Fireball hits {target} for {power} HP"

def valid_spell(target: str, power: int) -> bool:
    if power >= 10 and target:
        return True
    return False

if __name__ == "__main__":
    # Combiner:
    combined = spell_combiner(fireball, heal)
    print("Testing spell combiner...")
    print("Combined spell result: ", end="")
    print(*combined('Dragon', 12), sep=', ')

    print()
    # Amplifier:
    amplified = power_amplifier(fireball, 3)
    print("Testing power amplifier...")
    print(f"Original: {fireball('Dragon', 10)}")
    print(f"Amplified: {amplified('Dragon', 10)}")
    
    # print()
    # # Caster:
    # casted = conditional_caster(valid_spell, lightning)
    # print(casted('wolf', 20))
    