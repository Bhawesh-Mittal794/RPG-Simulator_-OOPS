import random
from character import Character


class Archer(Character):
    """Archer class with limited arrows and headshot attacks."""

    def __init__(self, name):
        super().__init__(
            name=name,
            health=120,
            attack=18,
            defense=7
        )

        self.__max_arrows = 20
        self.__arrows = 20

        self.__headshot_chance = 0.30
        self.__headshot_bonus = 15

    # ==================================================
    # Properties
    # ==================================================

    @property
    def arrows(self):
        return self.__arrows

    @property
    def max_arrows(self):
        return self.__max_arrows

    @property
    def headshot_chance(self):
        return self.__headshot_chance

    @property
    def headshot_bonus(self):
        return self.__headshot_bonus

    # ==================================================
    # Combat
    # ==================================================

    def attack(self, target):
        """
        Returns:
        {
            "damage": int,
            "headshot": bool,
            "no_arrows": bool
        }
        """

        if self.__arrows == 0:
            return {
                "damage": 0,
                "no_arrows": True
            }

        self.__arrows -= 1

        damage = self.attack_power
        headshot = False
        no_arrows = False
        

        if random.random() < self.headshot_chance:
            damage += self.headshot_bonus
            headshot = True

        return self._attack_result(
            damage=damage,
            headshot=headshot,
            no_arrows=no_arrows
        )

    # ==================================================
    # Arrow Management
    # ==================================================

    def reload(self, arrows):
        if arrows < 0:
            raise ValueError("Arrow count cannot be negative.")

        self.__arrows = min(
            self.__arrows + arrows,
            self.__max_arrows
        )

    # ==================================================
    # Level Up
    # ==================================================

    def level_up(self):
        super().level_up()

        self.__max_arrows += 5
        self.__arrows = self.__max_arrows

        self._attack_power += 2

    # ==================================================
    # Display
    # ==================================================

    def show_stats(self):
        stats = super().show_stats()

        return (
            stats[:-37]
            + f"Arrows    : {self.arrows}/{self.max_arrows}\n"
            + "===================================="
        )