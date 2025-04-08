from random import randint
import weapon as wp
from character import Character
from menu import Menu

class Bonus:
    def __init__(self, name: str, desc: str):
        """
        Initializes a Bonus object.

        Args:
            name (str): The name of the bonus.
            desc (str): The description of the bonus.
        """
        self.name = name
        self.desc = desc

class Weapon_box:
    def __init__(self, game):
        """
        Initializes a Weapon_box object.

        Args:
            game: The game object that the weapon box is associated with.
        """
        self.game = game
        self.weapon = [
            wp.Pumkin(),
            wp.Carrot(),
            wp.Leek(),
            wp.Apple(),
        ]
        self.nbrWeapon = len(self.weapon)

    def open(self) -> wp.Weapon:
        """
        Opens the weapon box and returns a random weapon.

        Returns:
            wp.Weapon: A randomly selected weapon from the box.
        """
        return self.weapon[randint(0, self.nbrWeapon - 1)]

class Bonus_box:
    def __init__(self, game):
        """
        Initializes a Bonus_box object.

        Args:
            game: The game object that the bonus box is associated with.
        """
        self.game = game
        self.bonus = [
            Bonus("attack", "You found a can of spinach! Your damage is increasing by 1"),
            Bonus("heal", "You found a banana! You gain 1 hp"),
            Bonus("shield", "You found nutshell! Your shield increases by 1"),
            Bonus("blindness", "You just ate a rotten carrot! You lost 1 damage per attack"),
            Bonus("rust", "Your shield is rotting! Your shield lost 1 protection")
        ]
        self.nbrbonus = len(self.bonus)

    def open(self, character: Character):
        """
        Opens the bonus box and applies a random bonus to the character.

        Args:
            character (Character): The character to apply the bonus to.

        Returns:
            Bonus: The bonus that was applied to the character.
        """
        choice = self.bonus[randint(0, self.nbrbonus - 1)]
        match choice.name:
            case "heal":
                character.hp += 1
            case "attack":
                character.weapon.damage += 1
            case "shield":
                character.shield += 1
            case "blindness":
                character.weapon.damage -= 1
            case "rust":
                character.shield -= 1

        return choice

class Mystery_Box_Menu(Menu):
    def __init__(self, game):
        """
        Menu where the player discover new objects
        Initializes a Mystery_box object.

        Args:
            game: The game object that the menu is associated with.
        """
        self.res = Weapon_box(game).open()
        self.bonus = Bonus_box(game).open(game.character)
        game.character.weapon = self.res
        super().__init__(
            f"====== Weapon Box ! ======\nYou just found a weapon box!\nYou found a {self.res.name}!\nStat: {self.res.damage} damages\n\n====== Bonus Box ! ======\nYou just found a Bonus box!\n{self.bonus.desc}\nAre you ready for your next fight ?",
            [
                "Yes !",
                "No, thanks, GET ME OUT OF HERE"
            ],
            [
                game.go_combat, 
                game.stop
            ]
        )
