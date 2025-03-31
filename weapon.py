class Weapon:
    """
    The Weapon class represents a weapon in the game with attributes for usage and damage.

    Attributes:
        possible_use (int): The number of times the weapon can be used.
        damage (int): The amount of damage the weapon inflicts.
        name (str): The name of the weapon.
    """

    def __init__(self, name: str, damage: int):
        """
        Initializes the Weapon instance with a name, number of uses, and damage.

        Args:
            name (str): The name of the weapon.
            time_use (int): The number of times the weapon can be used.
            damage (int): The amount of damage the weapon inflicts.
        """
        self.damage = damage
        self.name = name

    def __str__(self) -> str:
        """
        Returns the name of the weapon as its string representation.

        Returns:
            str: The name of the weapon.
        """
        return self.name

class Apple(Weapon):
    """
    A subclass of Weapon representing an Apple with specific attributes.
    """

    def __init__(self):
        """
        Initializes the Apple weapon with 1 use and 1 damage.
        """
        super().__init__("Apple", 1)

class Carrot(Weapon):
    """
    A subclass of Weapon representing a Carrot with specific attributes.
    """

    def __init__(self):
        """
        Initializes the Carrot weapon with 1 use and 2 damage.
        """
        super().__init__("Carrot", 1)

class Leek(Weapon):
    """
    A subclass of Weapon representing a Leek with specific attributes.
    """

    def __init__(self):
        """
        Initializes the Leek weapon with 2 uses and 1 damage.
        """
        super().__init__("Leek", 2)

class Pumkin(Weapon):
    """
    A subclass of Weapon representing a Pumpkin with specific attributes.
    """

    def __init__(self):
        """
        Initializes the Pumpkin weapon with 1 use and 3 damage.
        """
        super().__init__("Pumkin", 1)

