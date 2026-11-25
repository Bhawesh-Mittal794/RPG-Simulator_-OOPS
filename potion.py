from item import Item


class Potion(Item):
    """Represents a healing potion."""

    def __init__(self, name, heal_amount, description, value, rarity):
        if heal_amount <= 0:
            raise ValueError("Heal amount must be positive.")

        super().__init__(name, description, value, rarity)

        self.__heal_amount = heal_amount

    # ==================================================
    # Properties
    # ==================================================

    @property
    def heal_amount(self):
        return self.__heal_amount

    @property
    def consumable(self):
        return True

    # ==================================================
    # Potion Logic
    # ==================================================

    def use(self, character):
        """Heal the character and return True if used successfully."""
        character.heal(self.heal_amount)
        return True

    # ==================================================
    # Display
    # ==================================================

    def __str__(self):
        return f"{self.name} (+{self.heal_amount} HP, {self.rarity})"

    def __repr__(self):
        return (
            f"Potion("
            f"name='{self.name}', "
            f"heal_amount={self.heal_amount}, "
            f"rarity='{self.rarity}')"
        )

    def display_info(self):
        return (
            f"Potion: {self.name}\n"
            f"Heals: {self.heal_amount} HP\n"
            f"Rarity: {self.rarity}\n"
            f"Value: {self.value}\n"
            f"Description: {self.description}"
        )