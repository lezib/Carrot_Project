from os import system
from os import name as OS_NAME
from time import sleep
from weapon import *
from enemy import *

class Menu:
    """
    The Menu class represents a generic menu system with options and associated functions.

    Attributes:
        context (str): The text displayed before the options, providing context to the user.
        option (str): A formatted string of options presented to the user.
        functions (list): A list of functions corresponding to each option. Each function should return a Menu instance.
    """

    def __init__(self, context: str, options: list[str], functions):
        """
        Initializes the Menu instance with context, options, and corresponding functions.

        Args:
            context (str): The text displayed before the options.
            options (list[str]): A list of option descriptions.
            functions (list): A list of functions corresponding to each option.
        """
        self.context = context
        self.option = self.generate_text_menu(options)
        self.functions = functions

    def run(self):
        """
        Runs the menu, displaying options and handling user input until a valid choice is made.
        Returns the function corresponding to the chosen option.

        Returns:
            callable: The function corresponding to the chosen option.
        """
        index_choosed = None

        while index_choosed is None:  # Retry until the answer is valid
            system('cls' if OS_NAME == 'nt' else 'clear')  # Clear the terminal on Windows or Linux
            print(self.context)
            print(self.option)

            user_input = input(">>> ")

            # Verification of the input
            if not self.is_valid_input(user_input):
                self.error_show("Your input is not valid", 1)
                continue
            if user_input == "exit":
                return exit
            index_choosed = int(user_input) - 1

            if 0 > index_choosed or index_choosed >= len(self.functions):
                self.error_show("Your input is not valid", 1)
                index_choosed = None
            # End of verification of input

        print()
        return self.functions[index_choosed]  # Return the chosen function

    def error_show(self, text: str, time: float) -> None:
        """
        Displays an error message and pauses execution for a specified time.

        Args:
            text (str): The error message to display.
            time (float): The time to pause execution in seconds.
        """
        print(text)
        sleep(time)

    def generate_text_menu(self, option: list[str]) -> str:
        """
        Generates a formatted string of options with corresponding indices.

        Args:
            option (list[str]): A list of option descriptions.

        Returns:
            str: A formatted string of options.
        """
        i = 1
        res = ""
        for op in option:
            res += f"{i} : {op}\n"
            i += 1
        return res

    def is_valid_input(self, input: str) -> bool:
        """
        Checks if the user input is valid (either "exit" or a number corresponding to an option).

        Args:
            input (str): The user input to validate.

        Returns:
            bool: True if the input is valid, False otherwise.
        """
        if input == "exit":
            return True
        try:
            int(input)
            return True
        except:
            return False
class First_weapon_choice(Menu):
    """
    A subclass of Menu for choosing the first weapon in the game.
    """

    def __init__(self, game):
        """
        Initializes the First_weapon_choice menu with weapon options.

        Args:
            game (Game): The game instance.
        """
        super().__init__(
            "Choose your first weapon!",
            [
                "Carrot",
                "Apple",
                "Pumpkin",
                "Banana"
            ],
            [
                lambda: game.get_weapon(Carrot()),
                lambda: game.get_weapon(Apple()),
                lambda: game.get_weapon(Pumkin()),
                lambda: game.get_weapon(Leek())
            ]
        )

class Home_menu(Menu):
    """
    A subclass of Menu representing the home menu of the game.
    """

    def __init__(self, game):
        """
        Initializes the Home_menu with main game options.

        Args:
            game (Game): The game instance.
        """
        super().__init__(
            "===== HOME =====",
            [
                "New game",
                "Continue my game",
                "Exit"
            ],
            [
                game.newGame,
                game.load_save,
                game.stop
            ]
        )

class Debug_menu(Menu):
    """
    A subclass of Menu used for debugging purposes. All options lead back to the Home_menu.
    """

    def __init__(self, game, context: str):
        """
        Initializes the Debug_menu with debug options.

        Args:
            game (Game): The game instance.
            context (str): The context message to display.
        """
        super().__init__(
            f"===== Debug Menu ====\nYou landed in a debug Menu\nafter {context}",
            [
                "Go home",
                "Quit program"
            ],
            [
                game.go_home,
                game.stop
            ]
        )

class Combat_Menu(Menu) :
    """
    A temporary Menu to test Enemy
    """

    def __init__(self, game, enemy:Enemy) :
        self.game = game
        self.enemy = enemy
        super().__init__(
            f"{enemy.name} appeared !\n{enemy.ascii}\n\nWhat do you want to do !?",
            [
                "Attack !",
                "Eat Something",
                "Leave !"
            ],
            [
                self.attack,
                self.eat,
                self.leave
            ]
        )

    def attack(self) :
        dodged = self.enemy.try_dodge()
        if dodged :
            damage = 0
        else :
            damage = self.game.weapon.damage 
        return Debug_menu(self.game,f"trying attacking the {self.enemy.name}\n\nThe {self.enemy.name} dodge :{dodged}\nYou did {damage} damage to it")

    def eat(self) :
        return Debug_menu(self.game,"eating something")

    def leave(self) :
        return Debug_menu(self.game,f"Leaving the {self.enemy.name}")
