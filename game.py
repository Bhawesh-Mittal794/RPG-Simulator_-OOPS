import random
from copy import deepcopy

from warrior import Warrior
from mage import Mage
from archer import Archer

from battle import Battle

from data.enemy_data import get_enemy
from data.boss_data import get_boss, is_boss_level

from data.weapon_data import WEAPONS
from data.potion_data import POTIONS


class Game:

    def __init__(self):

        self.__player = None

        self.__current_level = 1

    # ==================================================
    # Properties
    # ==================================================

    @property
    def player(self):
        return self.__player

    @property
    def current_level(self):
        return self.__current_level

    # ==================================================
    # Player Creation
    # ==================================================

    def create_player(self):

        print("=" * 45)
        print("        RPG BATTLE SIMULATOR")
        print("=" * 45)

        name = input("Enter your character name: ").strip()

        while True:

            print("\nChoose Your Class")
            print("1. Warrior")
            print("2. Mage")
            print("3. Archer")

            choice = input("Choice : ").strip()

            if choice == "1":
                self.__player = Warrior(name)
                break

            elif choice == "2":
                self.__player = Mage(name)
                break

            elif choice == "3":
                self.__player = Archer(name)
                break

            else:
                print("Invalid Choice!")

    # ==================================================
    # Starter Items
    # ==================================================

    def give_starter_items(self):

        print("\nReceiving Starter Items...")

        starter_weapon = deepcopy(
            WEAPONS["Wooden Sword"]
        )

        self.player.equip_weapon(starter_weapon)

        self.player.inventory.add_potion(
            "Small Healing Potion"
        )

        self.player.inventory.add_potion(
            "Small Healing Potion"
        )

        print(f"Equipped: {starter_weapon.name}")
        print("Received: 2 Small Healing Potions")

    # ==================================================
    # Setup
    # ==================================================

    def setup(self):

        self.create_player()

        self.give_starter_items()

        print("\nYour Adventure Begins!")

    # ==================================================
    # Rewards
    # ==================================================

    def reward_player(self, enemy):

        print("\n" + "=" * 45)
        print("Battle Rewards")
        print("=" * 45)

        # ---------------- XP ----------------

        xp = enemy.xp_reward

        print(f"Earned {xp} XP!")

        leveled_up = self.player.gain_exp(xp)

        if leveled_up:
            print("\n⭐ LEVEL UP! ⭐")
            print(f"You reached Level {self.player.level}!")

        # ---------------- Heal ----------------

        heal_amount = self.player.max_health // 4

        self.player.heal(heal_amount)

        print(f"Healed for {heal_amount} HP.")

        # ---------------- Loot ----------------

        if random.random() <= enemy.drop_chance:

            loot_type = random.choice(
                ["weapon", "potion"]
            )

            if loot_type == "weapon":

                self.drop_weapon()

            else:

                self.drop_potion()

        else:

            print("No loot dropped.")

    # ==================================================
    # Weapon Drops
    # ==================================================

    def drop_weapon(self):

        level = self.current_level

        if level <= 4:

            choices = [
                "Iron Sword"
            ]

        elif level <= 9:

            choices = [
                "Steel Sword"
            ]

        elif level <= 14:

            choices = [
                "Knight Blade"
            ]

        else:

            choices = [
                "Dragon Slayer"
            ]

        weapon_name = random.choice(choices)

        weapon = deepcopy(
            WEAPONS[weapon_name]
        )

        print(f"\nWeapon Found!")

        print(f"You obtained {weapon.name}!")

        while True:

            choice = input(
                "Equip now? (y/n): "
            ).lower()

            if choice == "y":

                try:
                    self.player.equip_weapon(weapon)

                    print(f"{weapon.name} equipped.")

                except ValueError:
                    print(
                        f"You are not high enough level to equip {weapon.name}."
                    )

                    self.player.inventory.add_weapon(weapon)

                    print(f"{weapon.name} added to inventory.")

                return

            elif choice == "n":

                self.player.inventory.add_weapon(
                    weapon
                )

                print(
                    f"{weapon.name} added to inventory."
                )

                return

            else:

                print("Invalid choice.")

    # ==================================================
    # Potion Drops
    # ==================================================

    def drop_potion(self):

        level = self.current_level

        if level <= 4:

            potion = "Small Healing Potion"

        elif level <= 9:

            potion = random.choice([
                "Small Healing Potion",
                "Medium Healing Potion"
            ])

        else:

            potion = random.choice([
                "Medium Healing Potion",
                "Large Healing Potion"
            ])

        self.player.inventory.add_potion(
            potion
        )

        print(f"\nFound {potion}!")

    # ==================================================
    # Boss Rewards
    # ==================================================

    def boss_reward(self):

        print("\nBoss Defeated!")

        if self.current_level == 5:

            reward = deepcopy(
                WEAPONS["Steel Sword"]
            )

        elif self.current_level == 10:

            reward = deepcopy(
                WEAPONS["Knight Blade"]
            )

        else:

            reward = deepcopy(
                WEAPONS["Dragon Slayer"]
            )

        print(
            f"You received {reward.name}!"
        )

        self.player.inventory.add_weapon(
            reward
        )

        self.player.inventory.add_potion(
            "Large Healing Potion"
        )

        print(
            "Received Large Healing Potion!"
        )

    # ==================================================
    # Main Game Loop
    # ==================================================

    def start(self):

        self.setup()

        while self.current_level <= 15:

            print("\n" + "=" * 50)
            print(f"LEVEL {self.current_level}")
            print("=" * 50)

            # -----------------------------
            # Spawn Enemy / Boss
            # -----------------------------

            if is_boss_level(self.current_level):

                enemy = get_boss(self.current_level)

                print(
                    f"\n🔥 Boss Battle!"
                )

            else:

                enemy = get_enemy(self.current_level)

            print(
                f"\nA wild {enemy.name} appeared!"
            )

            battle = Battle(
                self.player,
                enemy
            )

            winner = battle.start()

            # -----------------------------
            # Player Lost
            # -----------------------------

            if winner != self.player:

                print("\nGame Over!")

                return

            # -----------------------------
            # Rewards
            # -----------------------------

            self.reward_player(enemy)

            if is_boss_level(self.current_level):

                self.boss_reward()

            # -----------------------------
            # Level Complete
            # -----------------------------

            print(
                f"\nLevel {self.current_level} Complete!"
            )

            self.__current_level += 1

            input(
                "\nPress Enter to continue..."
            )

        print("\n" + "=" * 50)
        print("🏆 CONGRATULATIONS!")
        print("=" * 50)

        print(
            f"\n{self.player.name} has completed the game!"
        )

        print(
            "\nThank you for playing!"
        )