from random import randint

class Enemy :
    def __init__(self,name:str, hp:int,damage:int,dodge:int,ascii:str) :
        """
        the more dodge is high the more the enemy can dodge
        """
        self.name = name
        self.hp = hp
        self.damage = damage
        self.dodge = dodge
        self.ascii = ascii
        pass

    def __str__(self) :
        return f"{ascii}\nPV : {self.hp}"

    def try_dodge(self) :
        return randint(0,10) <= self.dodge

    def attack(self):
        """
        Attack the player
        
        Return: the damage done to the player
        """
        if not randint(1, 100) <= 90:  # 10% miss chance
            return 0
        else :
            return self.damage * randint(1,2) # critical hit = damage * 2

    def hit(self, damage_received:int) -> bool :
        """
        Reduce hp of the ennemy

        Args:
            damage_received (int)
            
        Return:
            bool: is ennemy still alive
        """
        self.hp -= damage_received
        return self.hp <= 0

class Boss(Enemy) :
    def __init__(self,name:str, hp:int,damage:int,dodge:int,ascii:str, heal:int) :
        super().__init__(name,hp,damage,dodge,ascii)
        self.heal = heal
        self.turn_counter = 0

    def attack(self) :
        """
        Attack the player and increase the self.turn_counter
        
        Return: the damage done to the player
        """
        self.turn_counter += 1
        if self.turn_counter % 2 == 0 : # trigger the heal every 2 turn
            self.hp += self.heal
        if not randint(1, 100) <= 90:  # 10% miss chance
            return 0
        else :
            return self.damage * randint(1,2) # critical hit = damage * 2

class Donut(Enemy) :
    def __init__(self) :
        super().__init__("donut",5,2,5,"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠠⠤⠄⠀⠒⠒⠒⠒⠒⠒⠀⠤⠤⢄⣀\n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⠔⠒⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠑⠒⠤⣀\n ⠀⠀⠀⠀⠀⠀⠀⢀⠔⠊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠢⣄\n ⠀⠀⠀⠀⠀⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⢄\n ⠀⠀⠀⢀⠔⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⢄\n ⠀⠀⢀⠎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢣⡀\n ⠀⢀⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢣\n ⠀⡘⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇\n ⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠻⠦⢄⣀⣤⣶⡦⠤⠒⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢱\n ⠀⡇⠀⢀⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼\n ⠀⢡⠀⡏⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⣇\n ⠀⢸⡀⢷⡀⢳⣀⣄⠀⢠⠶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⠁⣷⣿⡄\n  ⣸⡇⢨⣷⣄⠀⠘⡄⢸⠀⡇⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⢤⠀⠀⡔⢳⢰⣁⣞⡩⠞\n ⠘⣇⠻⠿⡿⣿⠷⡀⠱⣸⠄⢻⠀⠀⡼⠋⠈⠙⠢⡀⠀⠀⠀⢀⠔⠒⢦⡀⠀⠀⠀⠀⠀⠀⢀⡎⠀⢸⠀⡜⠀⣸⣾⢻\n ⠀⠘⠧⣤⣀⣀⣠⠾⢻⣿⢆⠀⢧⣀⡇⠀⠀⠀⠀⢱⡀⠀⣰⠁⠀⠀⠀⠳⣄⣀⠜⢉⠀⠀⡜⠀⢀⡎⢰⡧⢾⣋⣡⠞\n ⠀⠀⠀⠀⠀⠀⠀⠀⠸⣏⡛⢓⡦⣄⡀⠀⠀⠀⠀⠀⡇⠀⣇⠀⠀⠀⠀⠀⠀⠀⠀⣾⣠⡞⣀⣴⣿⡿⠛⠇⡸⠁\n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠀⠀⠈⠙⠒⢦⠤⢴⡇⠀⣿⣄⣀⣀⣀⡤⢤⣶⣿⡿⠛⠙⢦⣀⢀⣀⣀⠼⠃\n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⠀⠺⠇⠀⡾⠟⠀⡼⠃\n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⢄⣀⣀⣤⠴⠚⠁")


class Burger(Enemy) :
    def __init__(self) :
        super().__init__(
                "Burger",
                5,
                2,
                5,
                "Ascii Burger"
        )

class Frite(Enemy) :
    def __init__(self) :
        super().__init__(
                "Frite",
                5,
                2,
                5,
                "Ascii Frite"
        )

class Popcorn(Enemy) :
    def __init__(self) :
        super().__init__(
                "Popcorn",
                5,
                2,
                5,
                "Ascii Popcorn"
        )

class Bonbon(Enemy) :
    def __init__(self) :
        super().__init__(
                "Bonbon",
                5,
                2,
                5,
                "Ascii Bonbon"
        )

class Pizza(Enemy) :
    def __init__(self) :
        super().__init__(
                "Pizza",
                5,
                2,
                5,
                "Ascii Pizza"
        )

class Tacos(Enemy) :
    def __init__(self) :
        super().__init__(
                "Tacos",
                5,
                2,
                5,
                "Ascii Tacos"
        )
