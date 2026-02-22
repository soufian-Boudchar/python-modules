players = {
    "players": {
        "alice": {
            "items": {
                "pixel_sword": 1,
                "code_bow": 1,
                "health_byte": 1,
                "quantum_ring": 3
            },
            "total_value": 1875,
            "item_count": 6
        },
        "bob": {
            "items": {
                "code_bow": 3,
                "pixel_sword": 2
            },
            "total_value": 900,
            "item_count": 5
        },
    },
    "catalog": {
        "pixel_sword": {
            "type": "weapon",
            "value": 150,
            "rarity": "common"
        },
        "quantum_ring": {
            "type": "accessory",
            "value": 500,
            "rarity": "rare"
        },
        "health_byte": {
            "type": "consumable",
            "value": 25,
            "rarity": "common"
        },
        "data_crystal": {
            "type": "material",
            "value": 1000,
            "rarity": "legendary"
        },
        "code_bow": {
            "type": "weapon",
            "value": 200,
            "rarity": "uncommon"
        }
    }
}


def inventory(catalog, player):
    summary = dict(total=0, weapon=0, consumable=0, accessory=0)

    for item_name, quantity in player["items"].items():
        item = catalog[item_name]

        item_data = {
            "type": item["type"],
            "rarity": item["rarity"],
            "value": item["value"],
            "quantity": quantity,
            "total": quantity * item["value"]
        }
        summary[item_data["type"]] += quantity
        print(
            f"{item_name} ({item_data['type']}, {item_data['rarity']}): {item_data['quantity']}x @ {item_data['value']} gold each = {item_data['total']} gold"
        )
    print(f"\nInventory value: {player['total_value']} gold")
    print(f"Item count: {player['item_count']} items")
    print(
        f"Categories: weapon({summary['weapon']}) consumable({summary['consumable']}) accessory({summary['accessory']})"
    )


def transaction():
    print("\n=== Transaction: Alice gives Bob 2 health_bytes ===")
    players["players"]["alice"]["items"]["health_byte"] -= 1
    players["players"]["alice"]["total_value"] -= 25
    players["players"]["alice"]["item_count"] -= 1
    players["players"]["bob"]["items"].update(health_byte=1)


print("=== Player Inventory System ===\n")
print("=== Alice's Inventory ===")

inventory(players["catalog"], players["players"]["alice"])
transaction()
print("Transaction successful!\n")

print("=== Updated Inventories ===")
print(
    f"Alice health_bytes: {players['players']['alice']['items']['health_byte']}"
)
print(f"Bob health_bytes: {players['players']['bob']['items']['health_byte']}")

print("\n=== Inventory Analytics ===")
print(
    f"Most valuable player: Alice ({players['players']['alice']['total_value']} gold)"
)
print(f"Most items: Alice ({players['players']['alice']['item_count']} items)")
print(
    f"Rarest items: {list(players['catalog'].keys())[3]}, "
    f"{list(players['catalog'].keys())[1]}"
)