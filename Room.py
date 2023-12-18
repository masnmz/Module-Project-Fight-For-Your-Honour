class Room:
    def __init__(self, name, description, up='', down='', right='', left='', enemy=None, solved=False):
        """
        Initialize a Room object with specified attributes.
        :param name: The name of the room.
        :param description: The description of the room.
        :param up: The name of the room in the upward direction.
        :param down: The name of the room in the downward direction.
        :param right: The name of the room in the rightward direction.
        :param left: The name of the room in the leftward direction.
        :param enemy: An optional Enemy object present in the room.
        :param solved: A flag indicating whether the room's puzzle or challenge is solved.
        """
        self.name = name
        self.description = description
        self.up = up
        self.down = down
        self.left = left
        self.right = right
        self.enemy = enemy
        self.solved = solved
