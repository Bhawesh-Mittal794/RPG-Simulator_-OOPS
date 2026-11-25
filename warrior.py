import random
from character import Character


class Warrior(Character):
    """High-health melee fighter."""

    def __init__(self, name):
        super().__init__(
            name=name,
            health=150,
            attack=20,
            defense=10
        )

        # Warriors have higher critical chance
        self._crit_chance = 0.20

    def attack(self,target):
        """Return the damage dealt by the warrior."""
        damage = self.attack_power

        critical = random.random() < self.crit_chance

        if critical:
            damage *= 2
            critical = True

        return self._attack_result(
            damage=damage,
            critical=critical
        )

    def level_up(self):
        super().level_up()

        # Warrior-specific bonuses
        self._attack_power += 3
        self._defense += 1