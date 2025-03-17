from os import system
from os import name as OS_NAME
from time import sleep
from weapon import *

class Menu() :
    def __init__(self,context:str,options:list[str],functions) :
        """
        The context is the text printed before a the choice
        Options is a list of string to describe the possible choice
        Functions is a list of functions, the functions of the option n is at n-1 index
        And must return a type 'Menu'
        
        Exemple of use :
        def main_menu() :
        \ttext = [
        \t\t"Attack with carrot",
        \t\t"Dodge next attack",
        \t]
        \tfunctions = [lambda attack(carrot),dodge]
        \thandling_menu("Menu Principal",generate_text_menu(text),functions)
        
        To pass an argument in the function in the list use the lambda word before !
        """
        self.context = context
        self.option = self.generate_text_menu(options)
        self.functions = functions

    def run(self) :
        index_choosed = None

        while index_choosed == None: # retry until the answer is valid
            system('cls' if OS_NAME == 'nt' else 'clear') # clear the terminal linux or window
            print(self.context)
            print(self.option)

            user_input = input(">>> ")

            # Verification of the input
            if not self.is_valid_input(user_input) :
                self.error_show("Your input is not valid", 1)
                continue
            if user_input == "exit" :
                return exit
            index_choosed = int(user_input) - 1

            if 0 > index_choosed or index_choosed >= len(self.functions) :
                self.error_show("Your input is not valid", 1)
                index_choosed = None
            # End of verification of input

        print()
        return self.functions[index_choosed] # return the choosed function

    def error_show(self,text:str, time : float) -> None :
        print(text)
        sleep(time)
    
    def generate_text_menu(self,option : list[str]) -> str :
        """Auto format the option like this :
        1 : option1
        2 : option2
        ...
        """
        i = 1
        res = ""
        for op in option :
            res += f"{i} : {op}\n"
            i+=1
        return res

    def is_valid_input(self, input:str) :
        if (input == "exit") :
            return True
        try :
            int(input)
            return True
        except :
            return False


class First_weapon_choice(Menu) :
    def __init__(self,game): # put game for testing purpose
        super().__init__(
            "Choose your first weapon !",
            [
                "Carrot",
                "Apple",
                "Pumkin",
                "Banana"
            ],
            [
                lambda: game.get_weapon(Carrot()),
                lambda: game.get_weapon(Apple()),
                lambda: game.get_weapon(Pumkin()),
                lambda: game.get_weapon(Leek())
            ]
        )

class Home_menu(Menu) :
    def __init__(self,game) :
        super().__init__(
            "===== HOME =====",
            [
                "New game",
                "Continue my game",
                "Exit"
            ],
            [
                game.main_loop,
                lambda: print("oui"), First_weapon_choice(self),
                game.stop
            ]
        )

class Debug_menu(Menu) :
    """
    The purpose of this menu is for debugging the travel between menus, and all of its options lead to the Home_menu
    """
    def __init__(self,game,context:str):
        super().__init__(
            f"===== Debug Menu ====\nYou landed in a debug Menu\nafter {context}",
            [
                "Nice !",
                "This is bad :("
            ],
            [
                game.stop,
                game.stop
            ]
        )
