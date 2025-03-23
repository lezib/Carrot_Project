from os import system
from os import name as OS_NAME

from menu import *
from weapon import *

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

    def get_weapon(self, weapon: Weapon) -> Menu:
        """
        Sets the selected weapon and returns a debug menu with a message about the chosen weapon.

        Args:
            weapon (Weapon): The weapon to be selected.

        Returns:
            Menu: The debug menu instance with a message about the chosen weapon.
        """
        self.weapon = weapon
        # return Debug_menu(self, f"choosing your weapon : {self.weapon}")
        return Combat_Menu(self,Donut())

    def newGame(self) -> Menu:
        """
        Initializes a new game, setting up the save file, and returns the first weapon choice menu.

        Returns:
            Menu: The first weapon choice menu instance.
        """
        # Initialization of the saving file
        return First_weapon_choice(self)

    def load_save(self) -> Debug_menu :
        return Debug_menu(self,"loading a save")

    def go_home(self) -> Home_menu :
        return Home_menu(self)

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
