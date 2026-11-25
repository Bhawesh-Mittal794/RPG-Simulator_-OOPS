from weapon import Weapon

# ==================================================
# Weapon Data
# ==================================================

WEAPONS = {

    "Wooden Sword": Weapon(
        "Wooden Sword",
        "A basic wooden sword.",
        10,
        "Common",
        damage=5,
        weapon_type="Sword",
        critical_chance=0.05,
        required_level=1,
        durability=100
    ),

    "Iron Sword": Weapon(
        "Iron Sword",
        "A stronger iron sword.",
        30,
        "Uncommon",
        damage=10,
        weapon_type="Sword",
        critical_chance=0.08,
        required_level=3,
        durability=100
    ),

    "Steel Sword": Weapon(
        "Steel Sword",
        "Reliable steel weapon.",
        60,
        "Rare",
        damage=16,
        weapon_type="Sword",
        critical_chance=0.10,
        required_level=6,
        durability=100
    ),

    "Knight Blade": Weapon(
        "Knight Blade",
        "A weapon forged for knights.",
        120,
        "Epic",
        damage=24,
        weapon_type="Sword",
        critical_chance=0.15,
        required_level=10,
        durability=100
    ),

    "Dragon Slayer": Weapon(
        "Dragon Slayer",
        "Legendary blade capable of defeating dragons.",
        250,
        "Legendary",
        damage=35,
        weapon_type="Sword",
        critical_chance=0.20,
        required_level=15,
        durability=100
    )

}