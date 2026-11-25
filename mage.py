from character import Character


class Mage(Character):
    """Mage class with mana-based spell attacks."""

    def __init__(self, name):
        super().__init__(
            name=name,
            health=100,
            attack=15,
            defense=5
        )

        self.__max_mana = 100
        self.__mana = 100

        self.__spell_cost = 20
        self.__spell_bonus_damage = 25

    # ==================================================
    # Properties
    # ==================================================

    @property
    def mana(self):
        return self.__mana

    @property
    def max_mana(self):
        return self.__max_mana

    @property
    def spell_cost(self):
        return self.__spell_cost

    @property
    def spell_bonus_damage(self):
        return self.__spell_bonus_damage

    # ==================================================
    # Combat
    # ==================================================

    def attack(self, target):
        damage = self.attack_power
        spell_used = False

        if self.mana >= self.spell_cost:
            self.__mana -= self.spell_cost
            damage += self.spell_bonus_damage
            spell_used = True

        return self._attack_result(
            damage=damage,
            spell_used=spell_used
        )

    # ==================================================
    # Mana
    # ==================================================

    def restore_mana(self, amount):
        if amount < 0:
            raise ValueError("Mana restored cannot be negative.")

        self.__mana = min(
            self.__mana + amount,
            self.__max_mana
        )

    # ==================================================
    # Leveling
    # ==================================================

    def level_up(self):
        super().level_up()

        self.__max_mana += 20
        self.__mana = self.__max_mana

        self._attack_power += 2

    # ==================================================
    # Display
    # ==================================================

    def show_stats(self):
        stats = super().show_stats()

        return (
            stats[:-31]  # removes the last ====================================
            + f"Mana      : {self.mana}/{self.max_mana}\n"
            + "===================================="
        )