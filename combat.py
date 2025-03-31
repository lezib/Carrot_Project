from menu import Menu
from menu import Debug_menu
from enemy import Enemy

class Combat_Menu(Menu):
    """
    A temporary Menu to test Enemy.
    """

    def __init__(self, game, enemy: Enemy):
        """
        Initialize the Combat Menu with game and enemy details.

        Args:
            game: The game instance.
            enemy (Enemy): The enemy character.
        """
        self.game = game
        self.enemy = enemy
        self.character = game.character
        super().__init__(
            f"Enemy :{self.enemy.name}\n{self.enemy.ascii}\n\nYour Stats : \nHP : {self.character.hp} | Weapon damage : {self.character.weapon.damage}\n\n{enemy.name}'s Stats :\n HP : {self.enemy.hp} | Damage : {self.enemy.damage}\nWhat do you want to do !?",
            [
                f"Attack ! ({self.character.weapon.damage} damages)",
                f"Use special : {self.character.special_name}\n   Description : {self.character.special_desc}\n   Cooldown : {self.character.ability_threshold} turns."
            ],
            [
                self.attack,
                self.special,
            ]
        )

    def refreshContext(self):
        """
        Refresh the context display with updated stats.
        """
        self.context = f"Enemy: {self.enemy.name}\n{self.enemy.ascii}\n\nYour Stats : \nHP : {self.character.hp} | Weapon damage : {self.character.weapon.damage}\n\n{self.enemy.name}'s Stats :\n HP : {self.enemy.hp} | Damage : {self.enemy.damage}\nWhat do you want to do !?"

    def verify_health(self) -> int:
        """
        Verify the health status of both the character and the enemy.

        Returns:
            int: 1 if the enemy is defeated, -1 if the character is defeated, 0 otherwise.
        """
        if self.enemy.hp <= 0:
            return 1
        elif self.character.hp <= 0:
            return -1
        else:
            return 0

    def attack(self):
        """
        Perform an attack on the enemy and check the outcome.

        Returns:
            Menu: The next menu to display based on the outcome.
        """
        self.enemy.hit(self.game.character.attack())
        if self.verify_health() == 1:
            return Debug_menu(self.game, "You won :)")
        return self.hitPlayer()

    def special(self):
        """
        Use the character's special ability and check the outcome.

        Returns:
            Menu: The next menu to display based on the outcome.
        """
        if self.game.character.use_special():
            return self.hitPlayer()
        self.refreshContext()
        return self

    def hitPlayer(self):
        """
        Process the enemy's attack on the player and check the outcome.

        Returns:
            Menu: The next menu to display based on the outcome.
        """
        self.game.character.hit(self.enemy.attack())
        if self.verify_health() == -1:
            return Debug_menu(self.game, "You lost :(")
        else:
            self.refreshContext()
            return self
