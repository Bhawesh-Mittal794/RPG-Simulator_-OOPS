import random
from enemy import Enemy

# ==================================================
# Enemy Data
# Levels 1-15
# Boss fights occur at Levels 5, 10 and 15
# ==================================================

LEVEL_ENEMIES = {
    1: {
        "name": "Goblin",
        "health": 60,
        "attack": 12,
        "defense": 3,
        "xp_reward": 20,
        "drop_chance": 0.35,
        "crit_chance": 0.05
    },

    2: {
        "name": "Wolf",
        "health": 80,
        "attack": 16,
        "defense": 5,
        "xp_reward": 35,
        "drop_chance": 0.35,
        "crit_chance": 0.08
    },

    3: {
        "name": "Slime",
        "health": 105,
        "attack": 20,
        "defense": 7,
        "xp_reward": 50,
        "drop_chance": 0.40,
        "crit_chance": 0.10
    },

    4: {
        "name": "Bandit",
        "health": 130,
        "attack": 24,
        "defense": 9,
        "xp_reward": 70,
        "drop_chance": 0.45,
        "crit_chance": 0.12
    },

    6: {
        "name": "Skeleton",
        "health": 170,
        "attack": 30,
        "defense": 12,
        "xp_reward": 90,
        "drop_chance": 0.45,
        "crit_chance": 0.15
    },

    7: {
        "name": "Orc",
        "health": 210,
        "attack": 36,
        "defense": 15,
        "xp_reward": 120,
        "drop_chance": 0.50,
        "crit_chance": 0.18
    },

    8: {
        "name": "Dark Archer",
        "health": 250,
        "attack": 42,
        "defense": 18,
        "xp_reward": 150,
        "drop_chance": 0.55,
        "crit_chance": 0.20
    },

    9: {
        "name": "Shadow Assassin",
        "health": 300,
        "attack": 50,
        "defense": 22,
        "xp_reward": 180,
        "drop_chance": 0.60,
        "crit_chance": 0.22
    },

    11: {
        "name": "Fire Knight",
        "health": 360,
        "attack": 60,
        "defense": 26,
        "xp_reward": 220,
        "drop_chance": 0.65,
        "crit_chance": 0.25
    },

    12: {
        "name": "Dragonling",
        "health": 420,
        "attack": 68,
        "defense": 30,
        "xp_reward": 260,
        "drop_chance": 0.70,
        "crit_chance": 0.28
    },

    13: {
        "name": "Shadow Beast",
        "health": 490,
        "attack": 76,
        "defense": 35,
        "xp_reward": 310,
        "drop_chance": 0.75,
        "crit_chance": 0.30
    },

    14: {
        "name": "Ancient Golem",
        "health": 560,
        "attack": 85,
        "defense": 40,
        "xp_reward": 360,
        "drop_chance": 0.80,
        "crit_chance": 0.35
    }
}


# ==================================================
# Create Enemy
# ==================================================

def get_enemy(level):
    """
    Returns a fresh Enemy object for the given level.
    """

    if level not in LEVEL_ENEMIES:
        raise ValueError(f"No normal enemy exists for Level {level}.")

    enemy = LEVEL_ENEMIES[level]

    return Enemy(
        name=enemy["name"],
        health=enemy["health"],
        attack=enemy["attack"],
        defense=enemy["defense"],
        xp_reward=enemy["xp_reward"],
        drop_chance=enemy["drop_chance"],
        crit_chance=enemy["crit_chance"]
    )


# ==================================================
# Utility
# ==================================================

def is_boss_level(level):
    return level in (5, 10, 15)


def is_valid_level(level):
    return 1 <= level <= 15