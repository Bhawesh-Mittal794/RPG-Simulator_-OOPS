import random
from character import Character


class Enemy(Character):
    """Base class for all normal enemies."""

    def __init__(
        self,
        name,
        health,
        attack,
        defense,
        xp_reward,
        drop_chance=0.35,
        crit_chance=0.10
    ):

        super().__init__(
            name=name,
            health=health,
            attack=attack,
            defense=defense
        )

        if xp_reward < 0:
            raise ValueError("XP reward cannot be negative.")

        if not 0 <= drop_chance <= 1:
            raise ValueError("Drop chance must be between 0 and 1.")

        if not 0 <= crit_chance <= 1:
            raise ValueError("Critical chance must be between 0 and 1.")

        self.__xp_reward = xp_reward
        self._crit_chance = crit_chance
        self.__drop_chance = drop_chance

    # ==================================================
    # Properties
    # ==================================================

    @property
    def xp_reward(self):
        return self.__xp_reward

    @property
    def drop_chance(self):
        return self.__drop_chance

    # ==================================================
    # Combat
    # ==================================================

    def attack(self, target):
        damage = self.attack_power

        critical = False

        if random.random() < self.crit_chance:
            damage *= 2
            critical = True

        return self._attack_result(
            damage=damage,
            critical=critical
        )

    # ==================================================
    # Display
    # ==================================================

    def show_stats(self):
        stats = super().show_stats()

        return (
            stats[:-37]
            + f"XP Reward : {self.xp_reward}\n"
            + "===================================="
        )