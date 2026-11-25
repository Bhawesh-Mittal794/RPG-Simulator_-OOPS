from item import Item


class Weapon(Item):
    """Represents a weapon that can be equipped by a character."""

    def __init__(
        self,
        name,
        description,
        value,
        rarity,
        damage,
        weapon_type,
        critical_chance,
        required_level,
        durability
    ):

        if damage <= 0:
            raise ValueError("Damage must be positive.")

        # Critical chance stored as decimal
        # Example:
        # 0.05 = 5%
        # 0.25 = 25%
        if not 0 <= critical_chance <= 1:
            raise ValueError("Critical chance must be between 0 and 1.")

        if required_level < 1:
            raise ValueError("Required level must be at least 1.")

        if not 0 <= durability <= 100:
            raise ValueError("Durability must be between 0 and 100.")

        super().__init__(name, description, value, rarity)

        self.__damage = damage
        self.__weapon_type = weapon_type
        self.__critical_chance = critical_chance
        self.__required_level = required_level
        self.__durability = durability

    # ==================================================
    # Properties
    # ==================================================

    @property
    def damage(self):
        return 0 if self.is_broken() else self.__damage

    @property
    def weapon_type(self):
        return self.__weapon_type

    @property
    def critical_chance(self):
        return self.__critical_chance

    @property
    def required_level(self):
        return self.__required_level

    @property
    def durability(self):
        return self.__durability

    @property
    def sell_price(self):
        return self.value // 2

    # ==================================================
    # Weapon Logic
    # ==================================================

    def is_broken(self):
        return self.__durability == 0

    def use(self):
        """Decrease durability after every successful attack."""

        if self.is_broken():
            raise ValueError(f"{self.name} is broken and cannot be used.")

        self.__durability -= 1

    def repair(self):
        """Restore weapon durability to 100%."""

        self.__durability = 100

    # ==================================================
    # Information
    # ==================================================

    def display_info(self):
        status = "Broken" if self.is_broken() else "Usable"

        return (
            f"Weapon: {self.name}\n"
            f"Description: {self.description}\n"
            f"Rarity: {self.rarity}\n"
            f"Damage: {self.damage}\n"
            f"Weapon Type: {self.weapon_type}\n"
            f"Critical Chance: {self.critical_chance * 100:.0f}%\n"
            f"Required Level: {self.required_level}\n"
            f"Durability: {self.durability}%\n"
            f"Status: {status}"
        )

    # ==================================================
    # Magic Methods
    # ==================================================

    def __str__(self):
        return (
            f"{self.name} "
            f"({self.rarity}) "
            f"+{self.damage} ATK"
        )

    def __repr__(self):
        return (
            f"Weapon("
            f"name='{self.name}', "
            f"damage={self.damage}, "
            f"rarity='{self.rarity}', "
            f"durability={self.durability})"
        )