from boss import Boss


# ==================================================
# Boss Data
# Boss fights occur at Levels 5, 10 and 15
# ==================================================

LEVEL_BOSSES = {

    5: {
        "name": "Goblin King",
        "health": 220,
        "attack": 35,
        "defense": 15,
        "xp_reward": 150,
        "drop_chance": 1.0,
        "crit_chance": 0.15,
        "rage_gain": 25,
        "rage_threshold": 100
    },

    10: {
        "name": "Necromancer",
        "health": 500,
        "attack": 65,
        "defense": 28,
        "xp_reward": 350,
        "drop_chance": 1.0,
        "crit_chance": 0.20,
        "rage_gain": 30,
        "rage_threshold": 100
    },

    15: {
        "name": "Dragon Emperor",
        "health": 850,
        "attack": 100,
        "defense": 45,
        "xp_reward": 700,
        "drop_chance": 1.0,
        "crit_chance": 0.25,
        "rage_gain": 35,
        "rage_threshold": 100
    }

}


# ==================================================
# Create Boss
# ==================================================

def get_boss(level):
    """
    Returns a fresh Boss object for the given boss level.
    """

    if level not in LEVEL_BOSSES:
        raise ValueError(f"No boss exists for level {level}.")

    return Boss(**LEVEL_BOSSES[level])


# ==================================================
# Utility
# ==================================================

def is_boss_level(level):
    return level in LEVEL_BOSSES