class Item:
    def __init__(self, name, weight):
        """
        Initialising an Item object.
        :param name: The name of the item.
        :param weight: The weight of the item.
        return: None
        """
        self.name = name
        self.weight = weight


class Armor(Item):
    def __init__(self, name, weight, armor):
        """
        Initialize an Armor object, inheriting from Item.
        :param name: The name of the armor.
        :param weight: The weight of the armor.
        :param armor: The armor value of the armor.
        :return: None
        """
        super().__init__(name, weight)
        self.armor = armor


class Pot(Item):

    def __init__(self, name, weight):
        """
        Initialising a Pot object, inheriting from Item.
        :param name: The name of the pot.
        :param weight: The weight of the pot.
        """
        super().__init__(name, weight)
        self.bonus_hp = 30
        self.coin = 30


class Weapon(Item):

    def __init__(self, name, weight, damage):
        """
        Initialize a Weapon object, inheriting from Item.
        :param name: The name of the weapon.
        :param weight: The weight of the weapon.
        :param damage: The damage value of the weapon.
        """
        super().__init__(name, weight)
        self.damage = damage
