import random
import sys
from Item import Weapon, Armor
from Inventory import Inventory
from Room import Room
from Enemy import Enemy
from Market import Market
from Player import Player
from TextUI import TextUI
import logging

logging.basicConfig(filename='game_log.txt', level=logging.INFO)


class GamePlay:
    """
            GamePlay class represents the main game logic and flow.

            :param player: Player object as the player character.
            """
    def __init__(self, player):
        """
                Initialises the game
                :param player: Player object as the player character
                """
        # Setting up the player, market, inventory, and text effects and available items on the game.
        self.game_player = player
        self.market = Market(game_player)
        self.inventory = Inventory(game_player)
        self.text_ui = TextUI()
        self.item_list = [
            Weapon(name="Training Sword", weight=1, damage=3),
            Weapon(name="Thin Sword", weight=2, damage=5),
            Weapon(name="Basic Sword", weight=3, damage=7),
            Weapon(name="Improved Basic Sword", weight=4, damage=8),
            Weapon(name="Long Sword", weight=5, damage=10),
            Weapon(name="Blood Sword", weight=8, damage=15),
            Weapon(name="Death Master", weight=10, damage=20),
            Armor(name="Chest Armor", weight=3, armor=2),
            Armor(name="Cloth Armor", weight=10, armor=5),
            Armor(name="Leather Armor", weight=15, armor=15),
            Armor(name="Steel Armor", weight=20, armor=20)

        ]
        # Creating game map with different rooms with enemies as a dictionary
        self.game_map = {
            'f1': Room('Town Market', 'You are in the market\n.'
                                      'Every other shops except warrior market is closed\n. '
                                      'You can go to the first floor only.',
                       '', '', 'f2', '', enemy=None, solved=True),

            'f2': Room('Floor 1', 'You are in the first floor\n.',
                       '', '', 'f3', 'f1',
                       enemy=Enemy(name="Bandit", hp=15, damage=random.randint(1, 5),
                                   item=self.item_list[0], coin=10)),

            'f3': Room('Floor 2', 'You are in the second floor\n.',
                       '', '', 'f4', 'f2',
                       enemy=Enemy(name="Experienced Bandit", hp=20, damage=random.randint(1, 10),
                                   item=self.item_list[1], coin=20)),

            'f4': Room('Floor 3', 'You are in the third floor\n.',
                       '', 'f5', '', 'f3',
                       enemy=Enemy(name="Bandit Leader", hp=25, damage=random.randint(1, 15),
                                   item=self.item_list[7], coin=30)),

            'f5': Room('Floor 4', 'You are in the fourth floor\n.',
                       '', '', '', 'f6',
                       enemy=Enemy(name="Ninja", hp=30, damage=random.randint(1, 20),
                                   item=self.item_list[2], coin=40)),

            'f6': Room('Floor 5', 'You are in the fifth floor\n.',
                       'f4', '', '', 'f7',
                       enemy=Enemy(name="Black Belt Ninja", hp=35, damage=random.randint(1, 25),
                                   item=self.item_list[8], coin=40)),

            'f7': Room('Floor 6', 'You are in the sixth floor\n.',
                       '', '', 'f5', 'f8',
                       Enemy(name="Black Belt Ninja", hp=35, damage=random.randint(1, 25),
                             item=self.item_list[3], coin=50)),

            'f8': Room('Floor 7', 'You are in the seventh floor\n.',
                       '', 'f9', '', 'f7',
                       Enemy(name="Ninja Master", hp=40, damage=random.randint(1, 30),
                             item=self.item_list[4], coin=60)),

            'f9': Room('Floor 8', 'You are in the eighth floor\n.',
                       '', 'f10', '', '',
                       Enemy(name="Ninja Master", hp=40, damage=random.randint(1, 30),
                             item=self.item_list[5], coin=70)),

            'f10': Room('Floor 9', 'You are in the ninth floor\n.',
                        'f8', '', 'f11', '',
                        Enemy(name="Betrayer Knight", hp=50, damage=random.randint(1, 40),
                              item=self.item_list[9], coin=80)),

            'f11': Room('Floor 10', 'You are in the tenth floor\n.',
                        'f8', '', 'f12', '',
                        Enemy(name="Betrayer Knight", hp=50, damage=random.randint(1, 40),
                              item=self.item_list[10], coin=80)),

            'f12': Room('Floor 12', 'You are in the room of the traitor.\n'
                                    'Be ready for your last fight.\n'
                                    'Everything is going to be end now.\n',
                        '', '', '', '',
                        Enemy(name="Betrayer Knight Leader", hp=80, damage=random.randint(30, 60),
                              item=self.item_list[6], coin=120))
        }

    def title_screen_selections(self):
        """
        Options for the title screen display and user input processing
        :return:
        """
        #
        options = input('>').lower()
        logging.info(f'Player selected: {options}')  # Save the player's selection
        if options == 'play':
            self.text_ui.intro_text()
            inp = input("Please Enter the Number of Your Choice. \n")
            if inp == '1':
                self.text_ui.textui_print("Wise Choice!\n"
                                          "You have already had a suspect in your mind.\n"
                                          "You followed him, and you think that you found him.\n"
                                          "You are sure that traitor is the King's second favourite Knight.\n"
                                          "You decided to raid to his castle.\n")
                game_player.player_setup()
                self.start_game()
            elif inp == '2':
                self.text_ui.textui_print("You choose to night to fight for your honour. Game is over, coward!!")
                game_player.game_over = True
            else:
                self.text_ui.textui_print("Yo do not know what to choose. You have to start from beginning\n")
                self.title_screen()
        elif options == 'help':
            self.help()
            self.title_screen_selections()
        elif options == 'quit':
            sys.exit()
        else:
            print("Please Enter a Valid Command")
            self.title_screen_selections()

    def help(self):
        """
        Displays the help information and game map for the game
        :return:
        """
        print('----------------------------------------------')
        print('---- Welcome to the World of the Honour!! ----')
        print('----------------------------------------------')
        print('-     Write up, down, left, right to move      -')
        print('-     Type your commands to perform them-    -')
        print('-     Good luck and have fun                 -')
        print()

        self.text_ui.game_map_show()

    def title_screen(self):
        """
        Displays the title screen of the game.
        :return: None
        """
        print('----------------------------------------------')
        print('- Welcome to the Fight for Your Honour -------')
        print('----------------------------------------------')
        print('-                   -Play-                   -')
        print('-                   -Help-                   -')
        print('-                   -Quit-                   -')
        self.title_screen_selections()

    def start_game(self):
        """
        Starts the game and enters the main game loop.
        :return: None
        """
        print('-----------------------')
        print("-   Let's start now!  -")
        print('-----------------------')
        self.print_loc()

        while not self.game_player.game_over:
            self.prompt()

    def prompt(self):
        """
        Handles the user input during the game.
        :return: None
        """
        acceptable_interactions = ['move', 'go', 'travel', 'market', 'walk', 'inventory', 'quit', 'help']
        self.text_ui.textui_print('What would you like to do ?\n')
        for i in range(len(acceptable_interactions)):
            print(f'{acceptable_interactions[i]}', end=" ")
        print("\n")
        print("Select and write only one of the allowable actions")
        interaction = input('>').lower()

        while interaction not in acceptable_interactions:
            print('The action is not valid, try again.\n')
            # save the player's try for getting out from locked room
            logging.warning(f"Player entered invalid interaction: {interaction} is not in {acceptable_interactions}")
            interaction = input('>').lower()

        if interaction == 'quit':
            sys.exit()
        elif interaction in ['move', 'go', 'travel', 'walk']:
            self.move_player()
        elif interaction == 'market':
            self.game_player.location = 'f1'
            self.text_ui.textui_print("You are back in the market\n."
                                      "You noticed that warrior market is open?\n"
                                      "But market has only pots. You can only buy pots!!\n"
                                      "What do you want to do?\n")
            self.market.sell()
            self.prompt()

        elif interaction == 'inventory':
            print('Inventory')
            self.inventory.show_inventory()
            self.prompt()

        elif interaction == 'help':
            self.help()

    def move_player(self):
        """
        Method Documentation:
        Handles the movement of the player within the game map.
        :return: None
        """

        self.text_ui.textui_print("Where do you want to go \n"
                                  "Enter the direction only \n"
                                  "Enter Help for Map\n")
        dest = input("> ").lower()
        # Saves the movement direction
        logging.info(f'Player choose to move to: {dest}')
        if dest in ['up', 'north']:
            destination = self.game_map[game_player.location].up
            self.movement(destination)
        elif dest in ['down', 'south']:
            destination = self.game_map[game_player.location].down
            self.movement(destination)
        elif dest in ['right', 'east']:
            destination = self.game_map[game_player.location].right
            self.movement(destination)
        elif dest in ['left', 'west']:
            destination = self.game_map[game_player.location].left
            self.movement(destination)
        else:
            if dest == 'help':
                self.help()
            else:
                print('Unknown Direction. Cannot do things that are not known. Enter valid direction\n')
                # Saves the input for unknown direction.
                logging.warning(f'Unknown direction entered: {dest}')
                self.move_player()

    def movement(self, destination):
        """
        Handles the movement of the player to a specific destination.
        :param destination: The destination room identifier.
        :return: None
        """
        if destination and (self.game_map[game_player.location].solved is True):
            self.text_ui.textui_print(f'You have moved to the {destination}.\n')
            logging.info(f'Player moved to: {destination}')  # Saves the player's destination
            game_player.location = destination
            self.print_loc()
            if destination == 'f1':
                self.market.sell()

            if self.game_map[game_player.location].enemy:
                self.combat(game_player, self.game_map[game_player.location].enemy)

        elif not self.game_map[game_player.location].solved:
            self.text_ui.textui_print("Sorry. The doors is locked. If you want to leave you have to kill the enemy\n")
            logging.warning(f'Player tried to move while the door were locked: {destination}')  # Kilitli odadan çıkmayı kaydet
            self.combat(game_player, self.game_map[game_player.location].enemy)
        else:
            print('\n You cannot move in that direction.\n')

    def print_loc(self):
        """
        Prints the current location information.
        :return: None
        """
        self.text_ui.textui_print('\n' + ('-' * 15))
        self.text_ui.textui_print(f'\n-{game_player.location}-')
        self.text_ui.textui_print(f'\n-{self.game_map[game_player.location].description}-')
        self.text_ui.textui_print('\n' + ('-' * 15) + '\n')

    def player_attack(self, player, enemy):
        """
        Handles the player's attack during combat.
        :param player: Player object as the player character.
        :param enemy: Enemy object as the opponent.
        :return: int, damage dealt to the enemy
        """

        if player.weapon:
            damage = random.randint(1, 20) + player.weapon.damage
        else:
            damage = random.randint(1, 20)
        self.text_ui.textui_print(f'You rolled the twenty-sized dice. You give {damage} damage to your {enemy.name}\n')
        logging.info(f'Player give damage to {enemy.name}: {damage}')
        enemy.hp -= damage
        return damage

    def enemy_attack(self, player, enemy):
        """
        Handles the enemy's attack during combat.
        :param player: Player object representing the player character.
        :param enemy: Enemy object representing the opponent.
        :return: int, damage dealt to the player
        """
        damage = enemy.damage
        player.hp -= damage
        return damage

    def combat(self, player, enemy):
        """
        Handles the combat sequence between the player and the enemies.
        :param player: Player object as the player character.
        :param enemy: Enemy object as the opponent.
        :return: None
        """
        if enemy.hp > 0:
            self.text_ui.textui_print(f'You encounter with {enemy.name}, Health: {enemy.hp}.'
                                      f'What would you like to do?\n'
                                      f'1: Use Health Pot:\n'
                                      f'2: Attack.\n')
            _ = input("Enter the number of the action\n"
                      "> ")
            if _ == '1':
                if len(player.inventory) <= 0:
                    print("You do not have any item in your inventory\n ")
                    self.combat(player, enemy)

                elif not player.inventory == []:
                    for item in player.inventory:
                        if item.name == 'Health Pot':
                            self.inventory.use_pot(item)
                            __ = input("Would you like to use another health pot?\n"
                                       "> \n").lower
                            if __ == 'yes':
                                self.inventory.use_pot(item)
                                self.combat(player, enemy)
                            else:
                                self.combat(player, enemy)

                    if 'Health Pot' not in player.inventory:
                        print("You do not have any Health Pot in your inventory", end="")
                        logging.warning(f'Player tried to use pot without having it')
                        self.combat(player, enemy)

            elif _ == '2':
                while player.hp > 0 and enemy.hp > 0:
                    self.text_ui.textui_print(f'')
                    if player.hp > 0:
                        self.player_attack(player, enemy)
                        if enemy.hp > 0:
                            self.text_ui.textui_print(f'Enemy hp :{enemy.hp}\n')
                        else:
                            self.text_ui.textui_print(f'Enemy hp :{0}\n')
                    if enemy.hp > 0:
                        enemy_damage = self.enemy_attack(player, enemy)
                        self.text_ui.textui_print(f"Enemy gave {enemy_damage} damage to you\n")
                        if player.hp > 0:
                            self.text_ui.textui_print(f'Your health: {player.hp}\n')
                        else:
                            self.text_ui.textui_print(f'Your health: {0}\n')
                    if player.hp <= 0:
                        self.text_ui.textui_print(
                            f'You lost the battle. {enemy.name} killed you. You died before proofing your innocence\n')
                        logging.info(f'Player was killed by {enemy.name}: ')
                        print("""\
                                    GAME OVER
                                    
                        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
                        MMMMMMMMMMMM        MMMMMMMMMMMM
                        MMMMMMMMMM            MMMMMMMMMM
                        MMMMMMMMM              MMMMMMMMM
                        MMMMMMMM                MMMMMMMM
                        MMMMMMM                 MMMMMMMM
                        MMMMMMM                  MMMMMMM
                        MMMMMMM                  MMMMMMM
                        MMMMMMM    MMM    MMM    MMMMMMM
                        MMMMMMM   MMMMM   MMMM   MMMMMMM
                        MMMMMMM   MMMMM   MMMM   MMMMMMM
                        MMMMMMMM   MMMM M MMMM  MMMMMMMM
                        MMVKMMMM        M        MMMMMMM
                        MMMMMMMM       MMM      MMMMMMMM
                        MMMMMMMMMMMM   MMM  MMMMMMMMMMMM
                        MMMMMMMMMM MM       M  MMMMMMMMM
                        MMMMMMMMMM  M M M M M MMMMMMMMMM
                        MMMM  MMMMM MMMMMMMMM MMMMM   MM
                        MMM    MMMM M MMMMM M MMMM    MM
                        MMM    MMMM   M M M  MMMMM   MMM
                        MMMM    MMMM         MMM      MM
                        MMM       MMMM     MMMM       MM
                        MMM         MMMMMMMM      M  MMM
                        MMMM  MMM      MMM      MMMMMMMM
                        MMMMMMMMMMM  MM       MMMMMMM  M
                        MMM  MMMMMMM       MMMMMMMMM   M
                        MM    MMM        MM            M
                        MM            MMMM            MM
                        MMM        MMMMMMMMMMMMM       M
                        MM      MMMMMMMMMMMMMMMMMMM    M
                        MMM   MMMMMMMMMMMMMMMMMMMMMM   M
                        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
                        
                                GAME OVER
        
                        """)
                        player.game_over = True

                    if enemy.hp <= 0:
                        self.text_ui.textui_print(f'Congratulations. You won the battle and killed {enemy.name}\n')
                        logging.info(f'Player killed the {enemy.name}')
                        if enemy.item:
                            self.text_ui.textui_print(f'Enemy has dropped {enemy.item.name}\n')
                            self.inventory.item_pick_up(enemy)
                        self.add_coin(player, enemy)
                        self.text_ui.textui_print(f'You got {enemy.coins} coins from enemy\n')
                        logging.info(f'Player got coins from {enemy.name}: {enemy.coins}')
                        self.text_ui.textui_print(f'Your coins: {player.coins}\n')
                        logging.info(f'Player {player.coins}')
                        self.text_ui.textui_print(f'You have found a key on {enemy.name}. This key unlocks the door.\n')
                        self.game_map[game_player.location].solved = True

                        if game_player.location == 'f12':
                            self.text_ui.textui_print(f'You have killed the {enemy.name}. You find the last piece of'
                                                      f'the conspiracy letter. You are reading the conspiracy letter'
                                                      f'with surprised eyes. The {enemy.name} co-operate with the'
                                                      f'enemy of your kingdom. You After you read the conspiracy letter'
                                                      f',you went straight to the king. The king was surprised too. '
                                                      f'King thought that this conspiracy is a valid reason to declare '
                                                      f'a war! But, you have a better idea. You make a proposal to your'
                                                      f'king. You are going to  \n'
                                                      f'Press F12 to exit the game.\n')
                            self.game_player.game_over = True
            elif _ == 'market':
                self.movement("market")

            else:
                if _ not in ['exit', 'quit']:
                    print("Invalid Choice.")
                    logging.warning(f'Player entered wrong input for the fight scene: {_}')
                    self.combat(player, enemy)
                else:
                    sys.exit()

    def add_coin(self, player, enemy):
        """
        Adds coins obtained from defeating an enemy to the player's coins.
        :param player: Player object as the player character.
        :param enemy: Enemy object as the defeated opponent.
        :return: None
        """
        player.coins += enemy.coins


if __name__ == "__main__":
    # Creating a new Player instance to as the player character
    game_player = Player()
    # Creating a new GamePlay instance, initializing the game with the created player
    game = GamePlay(game_player)
    # Displaying the title screen and initiate the game
    game.title_screen()
