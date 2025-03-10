from os import system
from os import name as OS_NAME

from menu import *
from weapon import *

class Game :
    def __init__(self) -> None:
        self.running = True
        self.weapon = None
        self.next_event = None

        self.main_loop()
        pass

    def get_weapon(self,weapon:Weapon) -> None :
        self.weapon = weapon

    def main_loop(self) -> None :
        self.next_event = First_weapon_choice(self)

        while self.running :
            system('cls' if OS_NAME == 'nt' else 'clear')
            state = self.next_event.run()
            if state == 1 :
                self.running = False
            pass

i = Game()
