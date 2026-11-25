import random
from enemy import Enemy


class Boss(Enemy):
    """Represents a boss enemy with a rage mechanic."""

    def __init__(
            self,
            name,
            health,
            attack,
            defense,
            xp_reward,
            drop_chance=1.0,
            crit_chance=0.15,
            rage_gain=25,
            rage_threshold=100
    ):

        super().__init__(
            name=name,
            health=health,
            attack=attack,
            defense=defense,
            xp_reward=xp_reward,
            drop_chance=drop_chance,
            crit_chance=crit_chance
        )

        self.__rage = 0
        self.__rage_gain = rage_gain
        self.__rage_threshold = rage_threshold

    # ==================================================
    # Properties
    # ==================================================

    @property
    def rage(self):
        return self.__rage

    @property
    def rage_gain(self):
        return self.__rage_gain

    @property
    def rage_threshold(self):
        return self.__rage_threshold

    # ==================================================
    # Combat
    # ==================================================

    def attack(self, target):
        """
        Returns:
        {
            "damage": int,
            "critical": bool,
            "rage_attack": bool
        }
        """

        damage = self.attack_power

        critical = False
        rage_attack = False

        # Critical hit
        if random.random() < self.crit_chance:
            damage *= 2
            critical = True

        # Build rage
        self.__rage += self.__rage_gain

        # Rage attack
        if self.__rage >= self.__rage_threshold:
            damage *= 2
            self.__rage = 0
            rage_attack = True

        return self._attack_result(
            damage=damage,
            critical=critical,
            rage_attack=rage_attack
        )

    # ==================================================
    # Level Up
    # ==================================================

    def level_up(self):
        super().level_up()

        self._attack_power += 5
        self._defense += 3

    # ==================================================
    # Display
    # ==================================================

    def show_stats(self):
        stats = super().show_stats()

        return (
            stats
            + f"\nRage      : {self.rage}/{self.rage_threshold}"
        )

    # ==================================================
    # Magic Methods
    # ==================================================

    def __str__(self):
        return f"{self.name} (Boss)"

    def __repr__(self):
        return (
            f"Boss("
            f"name='{self.name}', "
            f"level={self.level}, "
            f"health={self.health}/{self.max_health})"
        )