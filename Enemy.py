class Enemy:
    def __init__(self, name: str, hp: int, damage: int, item, coin):
        """
        Represents an enemy in the game.
        :param name: str, the enemy's name.
        :param hp: int, the enemy's health.
        :param damage: int, the damage the enemy can deal.
        :param item: Item, the enemies' items.
        :param coin: int, the enemies' coins.
        """
        self.name = name
        self.hp = hp
        self.damage = damage
        self.item = item
        self.coins = coin
