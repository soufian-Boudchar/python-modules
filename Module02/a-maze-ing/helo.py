import random

my_list = ["A", "B", "C"]

def get_item_from_seed(lst, seed):
    random.seed(seed)        # deterministic seed
    return random.choice(lst)  # khdd element men list

# Examples
seeds = [18128312823, 1812831824, 123456789]

for s in seeds:
    print(f"Seed {s} → {get_item_from_seed(my_list, s)}")
