from abc import ABC, abstractmethod


class Item(ABC):
    """Base class for all collectible items."""

    VALID_RARITIES = (
        "Common",
        "Uncommon",
        "Rare",
        "Epic",
        "Legendary"
    )

    def __init__(self, name, description, value, rarity):

        if value < 0:
            raise ValueError("Value cannot be negative.")

        if rarity not in self.VALID_RARITIES:
            raise ValueError("Invalid rarity.")

        self.__name = name
        self.__description = description
        self.__value = value
        self.__rarity = rarity

    # ==================================================
    # Magic Methods
    # ==================================================

    def __str__(self):
        return f"{self.name} ({self.rarity})"

    def __repr__(self):
        return (
            f"{self.__class__.__name__}("
            f"name='{self.name}', "
            f"rarity='{self.rarity}')"
        )

    def __eq__(self, other):
        if not isinstance(other, Item):
            return False

        return (
            self.name == other.name
            and self.rarity == other.rarity
        )

    # ==================================================
    # Abstract Method
    # ==================================================

    @abstractmethod
    def use(self, *args, **kwargs):
        """Use the item. Subclasses decide what parameters they need."""
        pass

    # ==================================================
    # Properties
    # ==================================================

    @property
    def name(self):
        return self.__name

    @property
    def description(self):
        return self.__description

    @property
    def value(self):
        return self.__value

    @property
    def rarity(self):
        return self.__rarity

    @property
    def consumable(self):
        return False

    # ==================================================
    # Setters
    # ==================================================

    @description.setter
    def description(self, description):
        self.__description = description

    @value.setter
    def value(self, value):
        if value < 0:
            raise ValueError("Value cannot be negative.")
        self.__value = value

    @rarity.setter
    def rarity(self, rarity):
        if rarity not in self.VALID_RARITIES:
            raise ValueError("Invalid rarity.")
        self.__rarity = rarity

    # ==================================================
    # Display
    # ==================================================

    def display_info(self):
        return (
            f"Name: {self.name}\n"
            f"Description: {self.description}\n"
            f"Value: {self.value}\n"
            f"Rarity: {self.rarity}"
        )