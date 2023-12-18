import unittest
from Player import Player
from Room import Room
from Enemy import Enemy
from Item import Item, Armor, Weapon, Pot
from Inventory import Inventory
from TextUI import TextUI
from Market import Market


class TestPlayer(unittest.TestCase):
    """
    Test class for the Player class.
    """

    def setUp(self):
        """
        Set up the Player object for testing.
        :return: None
        """
        self.player = Player()
        self.player.name = "Alp"

    def test_player(self):
        """
        Testing attributes of the Player class.
        :return: None
        """
        self.assertEqual(self.player.name, "Alp")
        self.assertEqual(self.player.hp, 120)
        self.assertEqual(self.player.damage, 0)
        self.assertEqual(self.player.inventory, [])
        self.assertEqual(self.player.capacity, 45)
        self.assertEqual(self.player.equipped_item, [])
        self.assertEqual(self.player.weapon, None)
        self.assertEqual(self.player.armor, None)
        self.assertEqual(self.player.location, 'f1')
        self.assertEqual(self.player.game_over, False)
        self.assertEqual(self.player.coins, 0)


class TestEnemy(unittest.TestCase):
    """
    Test class for the Enemy class.
    """

    def setUp(self):
        """
        Set up the Enemy object for testing.
        :return: None
        """
        self.enemy = Enemy('Trial Monster', 200, 200, 'Diamond', 1000)

    def test_enemy(self):
        """
        Testing attributes of the Enemy class.
        """
        self.assertEqual(self.enemy.name, 'Trial Monster')
        self.assertEqual(self.enemy.hp, 200)
        self.assertEqual(self.enemy.damage, 200)
        self.assertEqual(self.enemy.item, 'Diamond')
        self.assertEqual(self.enemy.coins, 1000)


class TestRoom(unittest.TestCase):
    """
    Test class for the Room class.
    """

    def setUp(self):
        """
        Setting up the Room object for testing.
        :return: None
        """
        self.room = Room('Test Room', 'Trial Description', 'up', 'down', 'right', 'left',
                         enemy=Enemy('Monster', 100, 20, 'Gold', 100))

    def test_room(self):
        """
        Testing attributes of the Room class.
        :return: None
        """
        self.assertEqual(self.room.name, "Test Room")
        self.assertEqual(self.room.description, "Trial Description")
        self.assertEqual(self.room.up, 'up')
        self.assertEqual(self.room.down, 'down')
        self.assertEqual(self.room.right, 'right')
        self.assertEqual(self.room.left, 'left')
        self.assertEqual(self.room.enemy.name, 'Monster')
        self.assertEqual(self.room.enemy.hp, 100)
        self.assertEqual(self.room.enemy.damage, 20)
        self.assertEqual(self.room.enemy.item, 'Gold')
        self.assertEqual(self.room.enemy.coins, 100)

    def test_room_initialization(self):
        """
        Test room initialization with some parameters.
        :return: None
        """
        room = Room(name='Living Room', description='A cozy place')
        assert room.name == 'Living Room'
        assert room.description == 'A cozy place'


class TestItem(unittest.TestCase):
    """
        Test class for the Item, Weapon, Armor, and Pot classes.
        :return: None
        """

    def setUp(self):
        """
        Set up Item objects for testing.
        :return: None
        """
        self.item = Item('Trial Item', 100)
        self.sword = Weapon('Test Sword', 1000, 1000)
        self.armor = Armor('Test Armor', 1000, 1000)
        self.pot = Pot('Test Pot', 10)

    def test_item(self):
        """
        Test various attributes of the Item class.
        :return: None
        """
        self.assertEqual(self.item.name, 'Trial Item')
        self.assertEqual(self.item.weight, 100)

    def test_sword(self):
        """
        Testing various attributes of the Weapon class.
        :return: None
        """
        self.assertEqual(self.sword.name, 'Test Sword')
        self.assertEqual(self.sword.weight, 1000)
        self.assertEqual(self.sword.damage, 1000)

    def test_armor(self):
        """
        Testing attributes of the Armor class.
        :return: None
        """
        self.assertEqual(self.armor.name, 'Test Armor')
        self.assertEqual(self.armor.weight, 1000)
        self.assertEqual(self.armor.armor, 1000)

    def test_pot(self):
        """
        Testing attributes of the Pot class.
        :return: None
        """
        self.assertEqual(self.pot.name, 'Test Pot')
        self.assertEqual(self.pot.weight, 10)
        self.assertEqual(self.pot.coin, 30)
        self.assertEqual(self.pot.bonus_hp, 30)


class TestInventory(unittest.TestCase):
    """
    Test class for the Inventory class.
    :return: None
    """
    def setUp(self):
        """
        Setting up a mock Player object for testing Inventory.
        :return: None
        """
        self.player = Player()
        self.player.name = 'Test Player'
        self.player.capacity = 100
        self.player.coins = 100
        self.player.hp = 100
        self.inventory = Inventory(self.player)

    def test_inventory_item_pick_up(self):
        """
        Testing adding an item to the player's inventory
        :return: None
        """
        player = Player()
        inventory = Inventory(player)
        enemy = Enemy(name='Goblin', hp=20, damage=10, item=Weapon('Sword', 5, 15), coin=5)
        inventory.item_pick_up(enemy)
        assert len(player.inventory) == 1  # Expecting the player's inventory to have one item after picking up
        assert player.capacity < 45  # Expecting player's capacity to decrease after picking up an item

    def test_inventory_item_equip_weapon(self):
        """
        Testing equipping a weapon from the player's inventory.
        :return: None
        """
        player = Player()
        inventory = Inventory(player)
        weapon = Weapon(name='Sword', weight=10, damage=10)
        player.inventory.append(weapon)
        inventory.item_equip(0, weapon)
        assert player.weapon is not None

    def test_inventory_item_equip_armor(self):
        """
        Test equipping armor from the player's inventory.
        :return: None
        """
        player = Player()
        inventory = Inventory(player)
        armor = Armor(name='Body Armor', weight=15, armor=15)
        player.inventory.append(armor)
        inventory.item_equip(0, armor)
        assert player.armor is not None

    def test_inventory_add_pot_enough_capacity(self):
        """
        Testing adding a Pot to the player's inventory when there's enough capacity.
        :return: None
        """
        player = Player()
        inventory = Inventory(player)
        pot = Pot(name='Health Pot', weight=3)
        player.coins = 60
        player.capacity = 10
        inventory.add_pot(pot)
        assert len(player.inventory) >= 1  # Expecting the player to add a pot to the inventory

    def test_inventory_use_pot(self):
        """
        Testing using a Pot to increase the player's health.
        :return: None
        """
        player = Player()
        inventory = Inventory(player)
        pot = Pot(name='Health Elixir', weight=3)
        player.inventory.append(pot)
        initial_health = player.hp
        inventory.use_pot(pot)
        assert player.hp > initial_health  # Expecting the player's health to increase after using a pot


class TestMarket(unittest.TestCase):
    """
    Test class for the Market class.
    """

    def test_market_check_coins(self):
        """
        Test checking the player's coins in the market.
        :return: None
        """
        player = Player()
        market = Market(player)
        player.coins = 30
        market.check_coins(player)
        assert len(player.inventory) == 1


class TestTextUI(unittest.TestCase):
    """
    Test class for the TextUI class.
    """
    def test_textui_print(self):
        """
        Test printing a message using the TextUI class.
        :return: None
        """
        text_ui = TextUI()
        text_ui.textui_print('Hello, World!')


if __name__ == '__main__':
    unittest.main()
