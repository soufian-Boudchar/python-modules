p = {
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
    _sum = {
        "total": 0,
        "weapon": 0,
        "consumable": 0,
        "accessory": 0
    }

    for item_name, quantity in player["items"].items():
        item = catalog[item_name]

        data = {
            "type": item["type"],
            "rarity": item["rarity"],
            "value": item["value"],
            "quantity": quantity,
            "total": quantity * item["value"]
        }
        _sum[data["type"]] += quantity
        print(f"{item_name} ({data['type']}, {data['rarity']}): ", end="")
        print(f"{data['quantity']}x @ {data['value']} gold each ", end="")
        print(f"= {data['total']} gold")

    print(f"\nInventory value: {player['total_value']} gold")
    print(f"Item count: {player['item_count']} items")

    print(f"Categories: weapon({_sum['weapon']}) ", end="")
    print(f"consumable({_sum['consumable']}) ", end="")
    print(f"accessory({_sum['accessory']})")


def transaction() -> None:
    print("\n=== Transaction: Alice gives Bob 2 health_bytes ===")
    p["players"]["alice"]["items"]["health_byte"] -= 1
    p["players"]["alice"]["total_value"] -= 25
    p["players"]["alice"]["item_count"] -= 1
    p["players"]["bob"]["items"].update(health_byte=1)


print("=== Player Inventory System ===\n")
print("=== Alice's Inventory ===")

inventory(p["catalog"], p["players"]["alice"])
transaction()
print("Transaction successful!\n")

print("=== Updated Inventories ===")
print(
    f"Alice health_bytes: {p['players']['alice']['items']['health_byte']}"
)
print(f"Bob health_bytes: {p['players']['bob']['items']['health_byte']}")

print("\n=== Inventory Analytics ===")
print("Most valuable player: ", end="")
print(f"Alice ({p['players']['alice']['total_value']} gold)")
print(f"Most items: Alice ({p['players']['alice']['item_count']} items)")
print(
    f"Rarest items: {list(p['catalog'])[3]}, "
    f"{list(p['catalog'])[1]}"
)
