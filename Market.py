from Item import Pot
from TextUI import TextUI
import logging


class Market:

    def __init__(self, game_player):
        """
        Initialising a Market object.
        :param game_player: The player object associated with the market.
        :return: None
        """
        self.game_player = game_player
        self.pot = Pot("Health Pot", 2)
        self.text_ui = TextUI()

    def sell(self):
        """
        Prompt the player to visit the market, allowing them to buy pots.
        :return: None
        """
        print('Do you want to visit the market?\n'
              'Yes, No?')
        _ = input('>').lower()
        if _ == 'yes':
            print('-----------------------')
            self.text_ui.textui_print('- You are in the market. You see that only pots are left on the shelves\n'
                                      'Would you like to buy some pot?\n')
            __ = input('> ').lower()
            if __ == 'yes':
                self.check_coins(self.game_player)
                logging.info(f'Remaining capacity of the player {self.game_player.capacity}')
            else:
                self.text_ui.textui_print("You choose not to buy. You can continue to your adventure\n")
                self.game_player.prompt()

    def check_coins(self, player):
        """
        Check if the player has enough coins to buy a pot.
        :param player: The player object.
        :return: None
        """
        if player.coins < self.pot.coin:
            print('You do not have enough coins to buy pot\n')
            logging.warning(f'The player does not have enough coins to buy pot. Player Coins:{self.game_player.coins}, '
                            f'{self.pot.coin}.')
        elif player.coins >= self.pot.coin:
            print(f'You bought a pot for {self.pot.coin}')
            logging.info(f'Player bought a pot {self.game_player.coins}')
            player.coins -= self.pot.coin
            player.inventory.append(self.pot)
            print("Would you like to buy another?\n")
            _ = input('> ').lower()
            if _ == 'yes':
                self.check_coins(player)
