from typing import Callable

def mage_counter() -> Callable:
    count = 0
    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter

def spell_accumulator(initial_power: int) -> Callable:
    total_power = initial_power
    def accumulates(added_power: int) -> int:
        nonlocal total_power
        total_power += added_power
        return total_power
    return accumulates

def enchantment_factory(enchantment_type: str) -> Callable:
    _type_ = enchantment_type
    def enchantment(item_name: str):
        return f"{_type_} {item_name}"
    return enchantment

def memory_vault() -> dict[str, Callable]:
    def store(key: any, value: any) -> dict[any, any]:
        return {key: value}