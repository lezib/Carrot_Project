from os import system
from os import name as OS_NAME

from menu import *
from weapon import *
from character import Character
from combat import Combat_Menu

class Game:
    """
    The Game class represents the core game loop and manages the game's state and flow.

    Attributes:
        running (bool): A flag indicating whether the game is currently running.
        weapon (Weapon): The currently selected weapon in the game.
        debug (bool): A flag indicating whether debug mode is enabled.
    """

    def __init__(self, debug: bool = True) -> None:
        """
        Initializes the Game instance and starts the main game loop.

        Args:
            debug (bool): Whether to enable debug mode. Defaults to True.
        """
        self.running = None
        self.weapon = None
        self.character = None
        self.debug = debug

        self.main_loop()

    def stop(self) -> Home_menu:
        """
        Stops the game by setting the running flag to False and returns to the home menu.

        Returns:
            Home_menu: The home menu instance.
        """
        self.running = False
        return Home_menu(self)

    def newGame(self) -> Menu:
        """
        Initializes a new game, setting up the save file, and returns the first weapon choice menu.

        Returns:
            Menu: The first weapon choice menu instance.
        """
        # Initialization of the saving file
        return Choose_Character(self)

    def load_save(self) -> Debug_menu :
        return Debug_menu(self,"loading a save")

    def go_home(self) -> Home_menu :
        return Home_menu(self)

    def set_character(self,character:Character) :
        self.character = character
        return self.go_combat()

    def go_combat(self) :
        enemy_possible = [Donut(),Burger(),Frite(),Popcorn(),Bonbon(),Pizza(),Tacos()]
        return Combat_Menu(self,enemy_possible[randint(0,len(enemy_possible)-1)])

    def main_loop(self) -> None:
        """
        The main game loop that keeps the game running until the running flag is set to False.
        It clears the terminal, runs the current menu, and handles the chosen action.
        If debug mode is enabled, it pauses execution to allow for debugging.
        """
        self.running = True
        event_choice = Home_menu(self)

        while self.running:
            system('cls' if OS_NAME == 'nt' else 'clear')  # Clear the terminal on Windows or Linux

            action = event_choice.run()  # Executing the menu
            event_choice = action()  # Executing the function chosen

            if self.debug:  # Debug area to print whatever you want
                print("[BEGINNING OF DEBUG] ")
                input("[END OF DEBUG] type something to continue")

i = Game(False)
