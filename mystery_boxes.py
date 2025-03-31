from random import randint
import weapon as wp
from character import Character
from menu import Menu

class Bonus : 
    def __init__(self, name:str, desc:str) :
        self.name = name
        self.desc = desc

class Weapon_box :
    def __init__(self,game) :
        self.game = game
        self.weapon = [
            wp.Pumkin(),
            wp.Carrot(),
            wp.Leek(),
            wp.Apple(),
        ]
        self.nbrWeapon = len(self.weapon)

    def open(self) -> wp.Weapon:
        return self.weapon[randint(0,self.nbrWeapon - 1)]

class Bonus_box :
    def __init__(self,game) :
        self.game = game
        self.bonus = [
            Bonus("attack","You found a can of spinach ! Your damage is increasing by 1"),
            Bonus("heal", "You found a banana ! You gain 1 hp"),
            Bonus("shield", "You found nutshell ! Your shield increase by 1"),
            Bonus("blindness","You just ate a rotten carrot ! You lost 1 damage per attack"),
            Bonus("rust", "Your shield is rotting ! Your shield lost 1 protection")
        ]
        self.nbrbonus = len(self.bonus)

    def open(self, character:Character) :
        choice = self.bonus[randint(0,self.nbrbonus-1)]
        match choice.name :
            case "heal":
                character.hp += 1
            case "attack" :
                character.weapon.damage += 1
            case "shield" :
                character.shield += 1
            case "blindness" :
                character.weapon.damage -= 1
            case "rust" :
                character.shield -= 1

        return choice

class Weapon_box_Menu(Menu) :
    def __init__(self, game) :
        self.res = Weapon_box(game).open()
        game.character.weapon = self.res
        super().__init__(
            f"====== Weapon Box ! ======\nYou just found a weapon box !\nYou found a {self.res.name} !\nStat : {self.res.damage} damages ",
            [
                "OH! A Bonus Box !",
            ],
            [
                lambda : Bonus_box_Menu(game)
            ]
        )

class Bonus_box_Menu(Menu) :
    def __init__(self, game) :
        self.res = Bonus_box(game).open(game.character)
        super().__init__(
            f"====== Bonus Box ! ======\nYou just found a Bonus box !\n{self.res.desc}\n",
            [
                "Next Fight !",
            ],
            [
                game.go_combat
            ]
        )
        


