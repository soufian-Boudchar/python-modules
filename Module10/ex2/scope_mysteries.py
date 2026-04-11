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
    vault = {}


    def store(key: str, value: any) -> None:
        vault[key] = value

    def recall(key: str) -> None:
        return vault.get(key, "Memory not found")
    return {
        'store': store,
        'recall': recall
    }


if __name__ == "__main__":
    counter_a = mage_counter()
    counter_b = mage_counter()
    print("Testing mage counter...")
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")
    
    print()
    print("Testing spell accumulator...")
    base = spell_accumulator(100)
    print(f"Base 100, add 20: {base(20)}")
    print(f"Base 100, add 30: {base(30)}")
    
    print()
    print("Testing enchantment factory...")
    enchantment = enchantment_factory("Flaming")
    print(enchantment("Sword"))
    
    enchantment = enchantment_factory("Frozen")
    print(enchantment("Shield"))
    
    print()
    print("Testing memory vault...")
    memory = memory_vault()
    store = memory['store']
    recall = memory['recall']
    
    store('secret', 42)
    print(f"Store 'secret' = 42")
    print(f"Recall 'secret': {recall('secret')}")
    print(f"Recall 'unknown': {recall('unknown')}")