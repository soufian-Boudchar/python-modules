from typing import Callable, Any
import functools
from operator import add, mul


def spell_reducer(spells: list[int], operation: str) -> int:

    if not spells:
        return 0

    ops_dict = {"add": add, "multiply": mul, "max": max, "min": min}

    op_parsed = operation.strip().lower()

    if op_parsed not in ops_dict:
        raise ValueError("Invalid operation!!")

    return functools.reduce(ops_dict[op_parsed], spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    v1 = functools.partial(base_enchantment, power=50, element="Fire")
    v2 = functools.partial(base_enchantment, power=50, element="Ice")
    v3 = functools.partial(base_enchantment, power=50, element="Lightning")

    return {
        "Fire Enchantment": v1,
        "Ice Enchantment": v2,
        "Lightning Enchantment": v3
    }


@functools.lru_cache
def memoized_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:

    @functools.singledispatch
    def cast_spell(arg):
        return "Unknown spell type"

    @cast_spell.register(int)
    def _(arg: int):
        return f"Damage spell: {arg} damage"

    @cast_spell.register(str)
    def _(arg: str):
        return f"Enchantment: {arg}"

    @cast_spell.register(list)
    def _(arg: list):
        return f"Multi-cast: {len(arg)} spells"

    return cast_spell


if __name__ == "__main__":
    print("Testing spell reducer...")
    print(f"Sum: {spell_reducer([50, 50], 'add')}")
    print(f"Product: {spell_reducer([10, 24000], 'multiply')}")
    print(f"Max: {spell_reducer([40, 1], 'max')}")

    print("\nTesting memoized fibonacci...")
    fibbo_data = [0, 1, 10, 15]
    for i in fibbo_data:
        print(f"Fib({i}): {memoized_fibonacci(i)}")

    cast_spell = spell_dispatcher()
    print("\nTesting spell dispatcher...")
    print(cast_spell(42))
    print(cast_spell("fireball"))
    print(cast_spell([1, 2, 3]))
    print(cast_spell(1.2))
