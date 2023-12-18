from Item import Armor
from Item import Weapon
from Item import Pot
from Market import Market
import sys
import logging


class Inventory:
    def __init__(self, player):
        """
        Class Documentation:
        The inventory management for the player in the game.
        :param player: Player, the player associated with this inventory.
        :return: None
        """
        self.player = player
        self.market = Market(player)

    def show_inventory(self):
        """
        Displaying the player's inventory with options to view different item categories.
        return: None
        """
        print(f'{self.player.name.upper()}, Capacity: {self.player.capacity}, Coins: {self.player.coins}\n')
        if len(self.player.inventory) <= 0:
            print('There is no item')
        else:
            print(
                  "Select the inventory menu you would like to see.\n"
                  "1: Weapon Inventory\n"
                  "2: Armor Inventory\n"
                  "3: Pot Inventory\n")
            inventory_menu_selection = input("> ").lower()

            if inventory_menu_selection == '1':
                print('-----------------------')
                print("-   Weapon Inventory  -")
                print('-----------------------')
                print('Write full name of the item you want to equip')
                counter = 0
                for item in self.player.inventory:
                    if isinstance(item, Weapon):
                        counter += 1
                        print(f'{counter}.) name: {item.name}, weight: {item.weight}, damage. {item.damage}')

                _ = input('> ').lower()
                for index, item in enumerate(self.player.inventory):
                    if _ == item.name.lower():
                        self.item_equip(index, item)
                        print(f'{item.name} equipped')
                        logging.info(f'Player equipped  {item.name}')  # Save the equipped weapon

            elif inventory_menu_selection == '2':
                print('-----------------------')
                print("-   Armor Inventory   -")
                print('-----------------------')
                counter = 0
                print('Select the item you want to equip')

                for item in self.player.inventory:
                    if isinstance(item, Armor):
                        counter += 1
                        print(f' {counter}.) name: {item.name}, weight: {item.weight}, armor. {item.armor}')

                _ = input('> ').lower()
                for index, item in enumerate(self.player.inventory):
                    if _ == item.name.lower():
                        self.item_equip(index, item)
                        print(f'{item.name} equipped')
                        logging.info(f'Player equipped  {item.name}')  # Save the equipped armor
                        print(f' Your Health: {self.player.hp}')
                        logging.info(f'Player health after equipping armor  {item.name}')  # Save the changed health

            elif inventory_menu_selection == '3':
                print('-----------------------')
                print("-   Pot Inventory   -")
                print('-----------------------')
                counter = 0
                print('Select the item you want to equip')

                for item in self.player.inventory:
                    if isinstance(item, Pot):
                        counter += 1
                        print(f' {counter}.) name: {item.name}, weight: {item.weight}, health. {item.bonus_hp}')
                _ = input('> ').lower()
                for index, item in enumerate(self.player.inventory):
                    if _ == item.name.lower():
                        self.use_pot(item)
                        logging.info(f'Player used {item.name}')  # Save the pot usage
            else:
                if inventory_menu_selection not in ['exit', 'quit']:
                    print(f'Unkown Entry for Inventory Menu')
                    logging.warning(f'Player entered wrong input for the inventory selection: '
                                    f'{inventory_menu_selection}')
                    self.show_inventory()
                else:
                    sys.exit()

    def item_pick_up(self, enemy):
        """
        Asks the player if they want to pick up an item dropped by an enemy.
        :param enemy: Enemy, the enemy from which the item is dropped.
        :return: None
        """
        print(f'Do you want to take {enemy.item.name}?\n'
              f'Yes,No ?')
        answer = input(">").lower()
        if answer == 'yes' and self.player.capacity >= enemy.item.weight:
            self.player.capacity -= enemy.item.weight
            self.player.inventory.append(enemy.item)
            print(f'Your remaining capacity is {self.player.capacity}')
            logging.info(f'Remaining capacity of the player {self.player.capacity}')  # Save the equipped weapon
            print(f'{enemy.item.name} is added to your inventory')
            logging.info(f'Player picked {enemy.item.name} from {enemy.name} {self.player.capacity}')
        elif answer == 'yes' and self.player.capacity < enemy.item.weight:
            print("Sorry, item cannot be added your inventory")
            logging.warning(f'Item could not be added because of not enough player capacity {self.player.capacity}')

    def item_equip(self, index, item):
        """
        Asks the player if they want to equip a specific item from the inventory.
        :param index: int, the index of the item in the inventory.
        :param item: Item, the item to be equipped.
        :return: None
        """
        if len(self.player.inventory) > 0:
            print(f'Would you like to Equip the {item.name}\n'
                  f'Yes, No?\n')
            _ = input('> ').lower()
            if _ == 'yes':
                item_to_be_equipped = self.player.inventory.pop(index)
                if isinstance(item_to_be_equipped, Weapon):
                    if self.player.weapon:
                        self.item_change(item_to_be_equipped)
                    else:
                        self.player.weapon = item_to_be_equipped
                        self.player.capacity += self.player.weapon.weight
                if isinstance(item_to_be_equipped, Armor):
                    if self.player.armor:
                        self.item_change(item_to_be_equipped)
                    self.player.armor = item_to_be_equipped
                    self.player.capacity += self.player.armor.weight
                    self.player.hp += self.player.armor.armor
            else:
                pass

    def item_change(self, item):
        """
        Changes the equipped item based on the player's choice.
        :param item: Item, the item to be equipped.
        :return: None
        """

        if self.player.weapon is not None and isinstance(item, Weapon):
            self.player.capacity -= self.player.weapon.weight
            self.player.inventory.append(self.player.weapon)
            self.player.weapon = None
            self.player.weapon = item
            self.player.capacity += self.player.weapon.weight

        elif self.player.armor is not None and isinstance(item, Armor):
            self.player.capacity -= self.player.armor.weight
            self.player.hp -= self.player.armor.armor
            self.player.inventory.append(self.player.armor)
            self.player.armor = None
            self.player.armor = item
            self.player.capacity += self.player.armor.weight

    def add_pot(self, item):
        """
        Adds a health pot to the player's inventory.
        :param item: Pot, the health pot to be added.
        :return: None
        """
        self.market.check_coins(self.player)
        if self.player.capacity >= item.weight:
            self.player.capacity -= item.weight
            print(f'Your capacity is {self.player.capacity}')
            logging.info(f'Remaining capacity of the player after buying pot {self.player.capacity}')
            self.player.inventory.append(item)
        else:
            print('You do not have enough capacity to carry any items')
            logging.warning(f'Remaining capacity of the player. Player Capacity: {self.player.capacity}, '
                            f'Item weight: {item.weight}')

    def use_pot(self, item):
        """
        Uses a health pot from the player's inventory.
        :param item: Pot, the health pot to be used.
        return: None
        """
        if isinstance(item, Pot):
            self.player.capacity += item.weight
            self.player.inventory.remove(item)
            self.player.hp += item.bonus_hp
            print(f'You used Pot. {item.bonus_hp} is added to your health. Your Health is :{self.player.hp}')
            logging.info(f'Health of the player after using pot {self.player.hp}')
        else:
            print("You do not have any Health Pot in your inventory\n ")
            logging.warning(f'Player tried to use pot without having it')
