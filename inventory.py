from weapon import Weapon


class Inventory:
    """Stores all weapons and potions owned by the player."""

    POTION_TYPES = (
        "Small Healing Potion",
        "Medium Healing Potion",
        "Large Healing Potion",
    )

    def __init__(self):
        # Every weapon is a separate object
        self.__weapons = []

        # Potions stack by quantity
        self.__potions = {
            potion: 0 for potion in self.POTION_TYPES
        }

    # ==================================================
    # Properties
    # ==================================================

    @property
    def weapons(self):
        return self.__weapons.copy()

    @property
    def potions(self):
        return self.__potions.copy()

    @property
    def weapon_count(self):
        return len(self.__weapons)

    @property
    def potion_count(self):
        return sum(self.__potions.values())

    # ==================================================
    # Add Items
    # ==================================================

    def add_item(self, item):
        if isinstance(item, Weapon):
            self.add_weapon(item)
        else:
            raise TypeError("Unsupported item type.")

    def add_weapon(self, weapon):
        if not isinstance(weapon, Weapon):
            raise TypeError("Expected a Weapon.")

        self.__weapons.append(weapon)

    def add_potion(self, potion_name):
        if potion_name not in self.__potions:
            raise ValueError("Invalid potion.")

        self.__potions[potion_name] += 1

    # ==================================================
    # Remove Items
    # ==================================================

    def remove_weapon(self, weapon):
        if weapon in self.__weapons:
            self.__weapons.remove(weapon)
            return True

        return False

    def remove_potion(self, potion_name):
        if (
            potion_name in self.__potions
            and self.__potions[potion_name] > 0
        ):
            self.__potions[potion_name] -= 1
            return True

        return False

    # ==================================================
    # Get Items
    # ==================================================

    def get_weapon(self, weapon_name):
        for weapon in self.__weapons:
            if weapon.name.lower() == weapon_name.lower():
                return weapon

        return None

    def get_potion_quantity(self, potion_name):
        return self.__potions.get(potion_name, 0)

    # ==================================================
    # Utility
    # ==================================================

    def has_weapon(self, weapon_name):
        return self.get_weapon(weapon_name) is not None

    def has_potion(self, potion_name):
        return self.get_potion_quantity(potion_name) > 0

    def clear(self):
        self.__weapons.clear()

        for potion in self.__potions:
            self.__potions[potion] = 0

    # ==================================================
    # Display
    # ==================================================

    def show_weapons(self):
        if not self.__weapons:
            return "Weapons:\nNone"

        output = ["Weapons:"]

        for index, weapon in enumerate(self.__weapons, start=1):
            output.append(
                f"{index}. {weapon.name} "
                f"({weapon.rarity}) "
                f"[Durability: {weapon.durability}%]"
            )

        return "\n".join(output)

    def show_potions(self):
        output = ["Potions:"]

        found = False

        for potion, quantity in self.__potions.items():
            if quantity > 0:
                found = True
                output.append(f"{potion} x{quantity}")

        if not found:
            output.append("None")

        return "\n".join(output)

    def show_inventory(self):
        return (
            self.show_weapons()
            + "\n\n"
            + self.show_potions()
        )

    # ==================================================
    # Magic Methods
    # ==================================================

    def __len__(self):
        return self.weapon_count + self.potion_count

    def __str__(self):
        return (
            f"Inventory("
            f"Weapons={self.weapon_count}, "
            f"Potions={self.potion_count})"
        )

    def __repr__(self):
        return self.__str__()