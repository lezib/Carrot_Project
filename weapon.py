class Weapon :
    def __init__(self,name:str, time_use:int, damage:int) :
        self.possible_use = time_use
        self.damage = damage
        self.name = name

    def use(self) :
        self.possible_use -= 1

    def __str__(self) -> str:
        return self.name

class Apple(Weapon) :
    def __init__(self) :
        super().__init__("Apple",1,1)

class Carrot(Weapon) :
    def __init__(self) :
        super().__init__("Carrot",1,2)

class Leek(Weapon) :
    def __init__(self) :
        super().__init__("Leek",2,1)

class Pumkin(Weapon) :
    def __init__(self) :
        super().__init__("Pumkin",1,3)
