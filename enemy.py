from random import randint

class Enemy:
    def __init__(self, name: str, hp: int, damage: int, dodge: int, ascii: str):
        """
        Initialize an Enemy with basic attributes.

        Args:
            name (str): The name of the enemy.
            hp (int): The hit points of the enemy.
            damage (int): The damage the enemy can deal.
            dodge (int): The dodge score of the enemy.
            ascii (str): The ASCII art representation of the enemy.
        """
        self.name = name
        self.hp = hp
        self.damage = damage
        self.dodge = dodge
        self.ascii = ascii
        pass

    def __str__(self):
        """
        Return a string representation of the enemy.

        Returns:
            str: The ASCII art and HP of the enemy.
        """
        return f"{self.ascii}\nPV : {self.hp}"

    def try_dodge(self):
        """
        Attempt to dodge an incoming attack.

        Returns:
            bool: True if the dodge is successful, False otherwise.
        """
        return randint(0, 10) <= self.dodge

    def attack(self):
        """
        Attack the player.

        Returns:
            int: The damage done to the player.
        """
        if not randint(1, 100) <= 90:  # 10% miss chance
            return 0
        else:
            return self.damage * randint(1, 2)  # critical hit = damage * 2

    def hit(self, damage_received: int) -> bool:
        """
        Reduce the HP of the enemy.

        Args:
            damage_received (int): The damage received by the enemy.

        Returns:
            bool: True if the enemy is still alive, False otherwise.
        """
        self.hp -= damage_received
        return self.hp <= 0

class Boss(Enemy):
    def __init__(self, name: str, hp: int, damage: int, dodge: int, ascii: str, heal: int):
        """
        Initialize a Boss with additional healing ability.

        Args:
            name (str): The name of the boss.
            hp (int): The hit points of the boss.
            damage (int): The damage the boss can deal.
            dodge (int): The dodge score of the boss.
            ascii (str): The ASCII art representation of the boss.
            heal (int): The amount of HP the boss heals every 2 turns.
        """
        super().__init__(name, hp, damage, dodge, ascii)
        self.heal = heal
        self.turn_counter = 0

    def attack(self):
        """
        Attack the player and increase the turn counter.

        Returns:
            int: The damage done to the player.
        """
        self.turn_counter += 1
        if self.turn_counter % 2 == 0:  # trigger the heal every 2 turns
            self.hp += self.heal
        if not randint(1, 100) <= 90:  # 10% miss chance
            return 0
        else:
            return self.damage * randint(1, 2)  # critical hit = damage * 2

class Donut(Enemy):
    def __init__(self):
        """
        Initialize a Donut enemy with predefined attributes.
        """
        super().__init__(
            "donut",
            5,
            2,
            5,
            "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠠⠤⠄⠀⠒⠒⠒⠒⠒⠒⠀⠤⠤⢄⣀\n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⠔⠒⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠑⠒⠤⣀\n ⠀⠀⠀⠀⠀⠀⠀⢀⠔⠊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠢⣄\n ⠀⠀⠀⠀⠀⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⢄\n ⠀⠀⠀⢀⠔⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⢄\n ⠀⠀⢀⠎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢣⡀\n ⠀⢀⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢣\n ⠀⡘⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇\n ⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠻⠦⢄⣀⣤⣶⡦⠤⠒⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢱\n ⠀⡇⠀⢀⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼\n ⠀⢡⠀⡏⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⣇\n ⠀⢸⡀⢷⡀⢳⣀⣄⠀⢠⠶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⠁⣷⣿⡄\n  ⣸⡇⢨⣷⣄⠀⠘⡄⢸⠀⡇⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⢤⠀⠀⡔⢳⢰⣁⣞⡩⠞\n ⠘⣇⠻⠿⡿⣿⠷⡀⠱⣸⠄⢻⠀⠀⡼⠋⠈⠙⠢⡀⠀⠀⠀⢀⠔⠒⢦⡀⠀⠀⠀⠀⠀⠀⢀⡎⠀⢸⠀⡜⠀⣸⣾⢻\n ⠀⠘⠧⣤⣀⣀⣠⠾⢻⣿⢆⠀⢧⣀⡇⠀⠀⠀⠀⢱⡀⠀⣰⠁⠀⠀⠀⠳⣄⣀⠜⢉⠀⠀⡜⠀⢀⡎⢰⡧⢾⣋⣡⠞\n ⠀⠀⠀⠀⠀⠀⠀⠀⠸⣏⡛⢓⡦⣄⡀⠀⠀⠀⠀⠀⡇⠀⣇⠀⠀⠀⠀⠀⠀⠀⠀⣾⣠⡞⣀⣴⣿⡿⠛⠇⡸⠁\n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠀⠀⠈⠙⠒⢦⠤⢴⡇⠀⣿⣄⣀⣀⣀⡤⢤⣶⣿⡿⠛⠙⢦⣀⢀⣀⣀⠼⠃\n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⠀⠺⠇⠀⡾⠟⠀⡼⠃\n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⢄⣀⣀⣤⠴⠚⠁"
        )

class Burger(Enemy):
    def __init__(self):
        """
        Initialize a Burger enemy with predefined attributes.
        """
        super().__init__(
            "Burger",
            5,
            2,
            5,
            "Ascii Burger"
        )

class Frite(Enemy):
    def __init__(self):
        """
        Initialize a Frite enemy with predefined attributes.
        """
        super().__init__(
            "Frite",
            5,
            2,
            5,
            "Ascii Frite"
        )

class Popcorn(Enemy):
    def __init__(self):
        """
        Initialize a Popcorn enemy with predefined attributes.
        """
        super().__init__(
            "Popcorn",
            5,
            2,
            5,
            "Ascii Popcorn"
        )

class Bonbon(Enemy):
    def __init__(self):
        """
        Initialize a Bonbon enemy with predefined attributes.
        """
        super().__init__(
            "Bonbon",
            5,
            2,
            5,
            "Ascii Bonbon"
        )

class Pizza(Enemy):
    def __init__(self):
        """
        Initialize a Pizza enemy with predefined attributes.
        """
        super().__init__(
            "Pizza",
            5,
            2,
            5,
            "Ascii Pizza"
        )

class Tacos(Enemy):
    def __init__(self):
        """
        Initialize a Tacos enemy with predefined attributes.
        """
        super().__init__(
            "Tacos",
            5,
            2,
            5,
            "Ascii Tacos"
        )
