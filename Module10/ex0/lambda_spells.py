artifacts = [{
    'name': 'Fire Staff',
    'power': 92,
    'type': 'accessory'
}, {
    'name': 'Storm Crown',
    'power': 60,
    'type': 'accessory'
}, {
    'name': 'Crystal Orb',
    'power': 85,
    'type': 'relic'
}, {
    'name': 'Earth Shield',
    'power': 56,
    'type': 'accessory'
}]
mages = [{
    'name': 'Jordan',
    'power': 99,
    'element': 'ice'
}, {
    'name': 'Luna',
    'power': 61,
    'element': 'fire'
}, {
    'name': 'Ash',
    'power': 90,
    'element': 'lightning'
}, {
    'name': 'Nova',
    'power': 65,
    'element': 'water'
}, {
    'name': 'Jordan',
    'power': 99,
    'element': 'lightning'
}]
spells = ['heal', 'tornado', 'lightning', 'meteor']


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda x: x['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda x: x['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return map(lambda x: f"* {x} *", spells)


def mage_stats(mages: list[dict]) -> dict:
    max_power = max(mages, key=lambda x: x['power'])['power']
    min_power = min(mages, key=lambda x: x['power'])['power']
    avg_power = sum(map(lambda x: x['power'], mages)) / len(mages)

    return {
        'max_power': max_power,
        'min_power': min_power,
        'avg_power': avg_power
    }


def main() -> None:
    print("\nTesting artifact sorter...")
    nsor = artifact_sorter(artifacts)
    for x, y in zip(nsor, nsor[1:]):
        print(
            f"{x['name']} ({x['power']} power) comes "
            "before {y['name']} ({y['power']} power)"
        )

    print()

    for i in spell_transformer(spells):
        print(f"{i} ", end="")


main()
