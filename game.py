from os import system
from os import name as OS_NAME

from menu import *
from weapon import *

class Game :
    def __init__(self,debug:bool= True) -> None:
        self.running = None
        self.weapon = None
        self.debug = debug

        self.main_loop()
        pass

    def stop(self) -> Home_menu:
        self.running = False
        return Home_menu(self)

    def get_weapon(self,weapon:Weapon) -> Menu : # Little test function
        self.weapon = weapon
        return Debug_menu(self,f"choosing your weapon : {self.weapon}")

    def newGame(self) -> Menu:
        # initialisation of the saving file
        return First_weapon_choice(self)

    def main_loop(self) -> None :
        self.running = True
        event_choice = Home_menu(self)

        while self.running :
            system('cls' if OS_NAME == 'nt' else 'clear') # clear the terminal on window or linux

            action = event_choice.run() # Executing the menu
            event_choice = action() # Executing the function choosed

            if self.debug : # debug area to print whatever you want
                print("[BEGINNING OF DEBUG] ")
                input("[END OF DEBUG] type something to continue")

i = Game()
