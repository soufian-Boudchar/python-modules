from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main():
    print("=== DataDeck Tournament Platform ===\n")

    platform = TournamentPlatform()

    dragon = TournamentCard("dragon_001", "Fire Dragon", 5, "Legendary", 7, 3,
                            5, 1200)
    wizard = TournamentCard("wizard_001", "Ice Wizard", 4, "Epic", 4, 2, 4,
                            1150)

    print("Registering Tournament Cards...")
    platform.register_card(dragon)
    platform.register_card(wizard)

    print(f"{dragon.name} (ID: {dragon.card_id}):")
    d_stats = dragon.get_tournament_stats()
    print(f"Interfaces: {d_stats['interfaces']}")
    print(f"Rating: {d_stats['rating']}")
    print(f"Record: {d_stats['record']}\n")

    print(f"{wizard.name} (ID: {wizard.card_id}):")
    w_stats = wizard.get_tournament_stats()
    print(f"Interfaces: {w_stats['interfaces']}")
    print(f"Rating: {w_stats['rating']}")
    print(f"Record: {w_stats['record']}\n")

    print("Creating tournament match...")
    match_result = platform.create_match("dragon_001", "wizard_001")
    print(f"Match result: {match_result}\n")

    print("Tournament Leaderboard:")
    leaderboard = platform.get_leaderboard()
    for line in leaderboard:
        print(line)

    print("\nPlatform Report:")
    print(platform.generate_tournament_report())

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
