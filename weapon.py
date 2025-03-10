class Weapon :
    def __init__(self, time_use:int, damage:int) :
        self.possible_use = time_use
        self.damage = damage

    def use(self) :
        self.possible_use -= 1

class Apple(Weapon) :
    def __init__(self) :
        super().__init__(1,1)

class Carrot(Weapon) :
    def __init__(self) :
        super().__init__(1,2)

class Leek(Weapon) :
    def __init__(self) :
        super().__init__(2,1)

class Pumkin(Weapon) :
    def __init__(self) :
        super().__init__(1,3)
