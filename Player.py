import logging


class Player:
    def __init__(self):
        """
        Initialize a Player object with default attributes.

        Attributes:
        name: The name of the player.
        hp: The health points of the player.
        damage: The damage points of the player.
        inventory: A list to store items in the player's possession.
        capacity: The maximum weight capacity of the player's inventory.
        equipped_item: A list to store currently equipped items.
        weapon: The currently equipped weapon.
        armor: The currently equipped armor.
        location: The current location of the player.
        game_over: A flag indicating whether the game is over.
        coins: The amount of coins the player has.
        :return: None
        """
        self.name = ''
        self.hp = 120
        self.damage = 0
        self.inventory = []
        self.capacity = 45
        self.equipped_item = []
        self.weapon = None
        self.armor = None
        self.location = 'f1'
        self.game_over = False
        self.coins = 0

    def player_setup(self):
        """
        Set up the player by prompting for their name.
        :return: None
        """
        self.name = input("Please Enter Your Name:")
        logging.info(f'Name of the player: {self.name}')
