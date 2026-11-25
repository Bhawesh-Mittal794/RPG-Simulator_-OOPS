from data.potion_data import POTIONS
from boss import Boss


class Battle:
    """
    Handles the complete battle between the player and an enemy.
    """

    def __init__(self, player, enemy):
        self.__player = player
        self.__enemy = enemy

    # ==================================================
    # Properties
    # ==================================================

    @property
    def player(self):
        return self.__player

    @property
    def enemy(self):
        return self.__enemy

    # ==================================================
    # Battle Loop
    # ==================================================

    def start(self):

        print("\n" + "=" * 45)
        print(f"⚔️  {self.player.name} VS {self.enemy.name}")
        print("=" * 45)

        while self.player.alive and self.enemy.alive:

            self.display_status()

            self.player_turn()

            if self.check_winner():
                break

            self.enemy_turn()

            if self.check_winner():
                break

        print("\n" + "=" * 45)
        print("🏁 Battle Finished")
        print("=" * 45)

        self.display_status()

        if self.player.alive:

            print(f"\n🎉 {self.player.name} defeated {self.enemy.name}!")

            return self.player

        print(f"\n💀 {self.enemy.name} defeated {self.player.name}!")

        return self.enemy

    # ==================================================
    # Player Turn
    # ==================================================

    def player_turn(self):

        while True:

            print("\nYour Turn")
            print("1. Attack")
            print("2. Use Potion")
            print("3. Inventory")

            choice = input("Choose action: ").strip()

            if choice == "1":

                self.process_attack(
                    attacker=self.player,
                    defender=self.enemy
                )

                break

            elif choice == "2":

                if self.use_potion():
                    break

            elif choice == "3":

                if self.open_inventory():
                    break

            else:
                print("Invalid choice.")

    # ==================================================
    # Enemy Turn
    # ==================================================

    def enemy_turn(self):

        print(f"\n{self.enemy.name}'s Turn")

        self.process_attack(
            attacker=self.enemy,
            defender=self.player
        )

    # ==================================================
    # Process Attack
    # ==================================================

    def process_attack(self, attacker, defender):

        result = attacker.attack(defender)

        if result["no_arrows"]:
            print(f"{attacker.name} has no arrows left!")
            return

        damage = result["damage"]

        # ---------- Attack Messages ----------

        print(f"\n{attacker.name} attacks!")

        if result["critical"]:
            print("💥 Critical Hit!")

        if result["spell_used"]:
            print("🔥 Fireball Cast!")

        if result["headshot"]:
            print("🎯 Headshot!")

        if result["rage_attack"]:
            print("😡 Rage Attack!")

        # ---------- Weapon Durability ----------

        if attacker.weapon is not None:

            attacker.weapon.use()

            if attacker.weapon.is_broken():
                print(f"⚠️ {attacker.weapon.name} has broken!")

        # ---------- Damage ----------

        actual_damage = defender.take_damage(damage)

        print(f"{defender.name} took {actual_damage} damage.")

        # ---------- Boss Rage ----------

        if isinstance(attacker, Boss):

            print(
                f"Rage: "
                f"{attacker.rage}/"
                f"{attacker.rage_threshold}"
            )

    # ==================================================
    # Potion Handling
    # ==================================================

    def use_potion(self):

        inventory = self.player.inventory

        available_potions = [
            name
            for name, quantity in inventory.potions.items()
            if quantity > 0
        ]

        if not available_potions:
            print("\nNo potions available!")
            return False

        print("\nAvailable Potions:")

        for index, potion_name in enumerate(available_potions, start=1):

            quantity = inventory.potions[potion_name]
            heal = POTIONS[potion_name].heal_amount

            print(
                f"{index}. {potion_name} "
                f"(Heal: {heal} HP) "
                f"x{quantity}"
            )

        while True:

            choice = input("Choose potion (0 to cancel): ").strip()

            if choice == "0":
                return False

            if not choice.isdigit():
                print("Please enter a valid number.")
                continue

            choice = int(choice)

            if 1 <= choice <= len(available_potions):

                potion_name = available_potions[choice - 1]

                POTIONS[potion_name].use(self.player)

                inventory.remove_potion(potion_name)

                print(
                    f"\n{self.player.name} used "
                    f"{potion_name}!"
                )

                return True

            print("Invalid choice.")

    # ==================================================
    # Inventory Opening
    # ==================================================
    def open_inventory(self):

        weapons = self.player.inventory.weapons
    
        if not weapons:
            print("\nNo weapons in inventory.")
            return False

        print("\n========== INVENTORY ==========")

        current_weapon = self.player.weapon

        for index, weapon in enumerate(weapons, start=1):

            equipped = ""

            if current_weapon == weapon:
                equipped = " (Equipped)"

            print(
                f"{index}. {weapon.name}"
                f"{equipped}"
            )

            print(
                f"   Damage      : {weapon.damage}"
            )

            print(
                f"   Durability  : {weapon.durability}%"
            )

            print(
                f"   Required Lv : {weapon.required_level}"
            )

        print("0. Back")

        while True:

            choice = input(
                "\nChoose weapon: "
            ).strip()

            if choice == "0":
                return False

            if not choice.isdigit():
                print("Invalid choice.")
                continue

            choice = int(choice)

            if 1 <= choice <= len(weapons):

                weapon = weapons[choice - 1]

                try:

                    self.player.equip_weapon(weapon)

                    print(
                        f"\n{weapon.name} equipped!"
                    )

                    return True

                except ValueError as error:

                    print(error)

                    return False

            print("Invalid choice.")

    # ==================================================
    # Display Status
    # ==================================================

    def display_status(self):

        print("\n" + "-" * 45)

        print(
            f"{self.player.name}"
            f"\nHP : {self.player.health}/{self.player.max_health}"
        )

        if self.player.weapon is not None:

            print(
                f"Weapon : {self.player.weapon.name}"
            )

            print(
                f"Durability : "
                f"{self.player.weapon.durability}%"
            )

        if hasattr(self.player, "mana"):

            print(
                f"Mana : "
                f"{self.player.mana}/{self.player.max_mana}"
            )

        if hasattr(self.player, "arrows"):

            print(
                f"Arrows : "
                f"{self.player.arrows}/{self.player.max_arrows}"
            )

        print("\n------------------------------")

        print(
            f"{self.enemy.name}"
            f"\nHP : {self.enemy.health}/{self.enemy.max_health}"
        )

        if isinstance(self.enemy, Boss):

            print(
                f"Rage : "
                f"{self.enemy.rage}/{self.enemy.rage_threshold}"
            )

        print("-" * 45)

    # ==================================================
    # Winner
    # ==================================================

    def check_winner(self):

        if not self.player.alive:
            return self.enemy

        if not self.enemy.alive:
            return self.player

        return None