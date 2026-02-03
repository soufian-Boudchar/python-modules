alice = set(['first_kill', 'level_10', 'treasure_hunter', 'speed_demon'])
bob = set(['first_kill', 'level_10', 'boss_slayer', 'collector'])
charlie = set(['level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon', 'perfectionist'])
unique = alice.union(bob, charlie)
common = alice.intersection(bob, charlie)

print("=== Achievement Tracker System ===")
print(f"Player alice achievements: {alice}")
print(f"Player bob achievements: {bob}")
print(f"Player charlie achievements: {charlie}")

print("\n=== Achievement Analytics ===")
print(f"All unique achievements: {unique}")
print(f"Total unique achievements: {len(unique)}\n")

print(f"Common to all players: {common}")


alice_only = alice.difference(charlie.union(bob))
bob_only = bob.difference(alice.union(charlie))
charlie_only = charlie.difference(bob.union(alice))
rar = alice_only.union(bob_only).union(charlie_only)

print(f"Rare achievements (1 player): {rar}\n")

print(f"Alice vs Bob common: {alice.intersection(bob)}")
print(f"Alice unique: {alice.difference(bob)}")
print(f"Bob unique: {bob.difference(alice)}")