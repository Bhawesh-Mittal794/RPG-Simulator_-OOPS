from abc import ABC, abstractmethod
from weapon import Weapon
from inventory import Inventory


class Character(ABC):
    """Base class for all playable characters, enemies and bosses."""

    EXP_TO_LEVEL = 100
    BASE_CRIT_CHANCE = 0.05

    def __init__(self, name, health, attack, defense):
        if health <= 0:
            raise ValueError("Health must be positive.")

        if attack < 0:
            raise ValueError("Attack cannot be negative.")

        if defense < 0:
            raise ValueError("Defense cannot be negative.")

        self.__name = name
        self.__level = 1

        self._health = health
        self._max_health = health

        self._attack_power = attack
        self._defense = defense

        self.__exp = 0
        self.__alive = True

        self.__weapon = None
        self.__inventory = Inventory()

        self._crit_chance = self.BASE_CRIT_CHANCE

    # ==========================================================
    # Magic Methods
    # ==========================================================

    def __str__(self):
        return f"{self.name} (Level {self.level})"

    # ==========================================================
    # Properties
    # ==========================================================

    @property
    def name(self):
        return self.__name

    @property
    def health(self):
        return self._health

    @property
    def max_health(self):
        return self._max_health

    @property
    def attack_power(self):
        if self.weapon:
            return self._attack_power + self.weapon.damage
        return self._attack_power

    @property
    def defense(self):
        return self._defense

    @property
    def level(self):
        return self.__level

    @property
    def exp(self):
        return self.__exp

    @property
    def alive(self):
        return self.__alive

    @property
    def inventory(self):
        return self.__inventory

    @property
    def weapon(self):
        return self.__weapon

    @weapon.setter
    def weapon(self, weapon):
        self.equip_weapon(weapon)

    @property
    def crit_chance(self):
        weapon_bonus = 0

        if self.weapon:
            weapon_bonus = self.weapon.critical_chance

        return self._crit_chance + weapon_bonus

    @property
    def health_percentage(self):
        return (self.health / self.max_health) * 100

    # ==========================================================
    # Weapon Methods
    # ==========================================================

    def equip_weapon(self, weapon):

        if weapon is None:
            self.__weapon = None
            return

        if not isinstance(weapon, Weapon):
            raise TypeError("Invalid weapon.")

        if self.level < weapon.required_level:
            raise ValueError(
                f"Level {weapon.required_level} required to equip {weapon.name}."
            )

        # Already equipped
        if self.__weapon == weapon:
            print(f"{weapon.name} is already equipped.")
            return

        # Store old weapon
        old_weapon = self.__weapon

        # Equip new weapon
        self.__weapon = weapon

        # Remove new weapon from inventory if present
        self.inventory.remove_weapon(weapon)

        # Put old weapon back into inventory
        if old_weapon is not None:
            self.inventory.add_weapon(old_weapon)

    def unequip_weapon(self):
        self.__weapon = None

    # ==========================================================
    # Combat
    # ==========================================================

    @abstractmethod
    def attack(self, target):
        pass

    def take_damage(self, damage):

        if damage < 0:
            raise ValueError("Damage cannot be negative.")

        actual_damage = max(0, damage - self._defense)

        self._health = max(0, self._health - actual_damage)

        if self._health == 0:
            self.__alive = False

        return actual_damage

    def heal(self, amount):
        if not self.alive:
            return

        if amount < 0:
            raise ValueError("Heal amount cannot be negative.")

        self._health = min(
            self.health + amount,
            self.max_health
        )

    # ==========================================================
    # Experience
    # ==========================================================

    def gain_exp(self, xp):
        leveled_up = False
        if xp < 0:
            raise ValueError("XP cannot be negative.")

        self.__exp += xp

        while self.exp >= self.EXP_TO_LEVEL:
            self.__exp -= self.EXP_TO_LEVEL
            self.level_up()
            leveled_up = True

        return leveled_up

    def level_up(self):
        self.__level += 1

        self._max_health += 20
        self._health = self.max_health

        self._attack_power += 5
        self._defense += 2

    def revive(self):
        self.__alive = True
        self._health = self.max_health

    def restore_full_health(self):
        self._health = self.max_health

    # ==========================================================
    # Status
    # ==========================================================

    def get_status(self):
        return "Alive" if self.alive else "Dead"

    def _attack_result(
            self,
            damage=0,
            critical=False,
            spell_used=False,
            headshot=False,
            rage_attack=False,
            no_arrows=False
    ):
        return {
            "damage": damage,
            "critical": critical,
            "spell_used": spell_used,
            "headshot": headshot,
            "rage_attack": rage_attack,
            "no_arrows": no_arrows
        }

    def show_stats(self):
        weapon_name = self.weapon.name if self.weapon else "None"

        return f"""
========== CHARACTER STATS ==========
Name      : {self.name}
Level     : {self.level}
Health    : {self.health}/{self.max_health}
Attack    : {self.attack_power}
Defense   : {self.defense}
Weapon    : {weapon_name}
EXP       : {self.exp}/{self.EXP_TO_LEVEL}
Status    : {self.get_status()}
====================================
"""

    # ==========================================================
    # Future Extension Hooks
    # ==========================================================

    def special_attack(self, target):
        return False

    def on_death(self):
        pass