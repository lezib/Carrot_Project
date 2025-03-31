from random import randint

from weapon import Weapon

class Character:
    def __init__(self, name: str, hp: int, shield: int, dodge_score: int, ability_threshold: int, special_name: str, special_desc: str, weapon: Weapon):
        """
        Initialize a Character with basic attributes and a weapon.

        Args:
            name (str): The name of the character.
            hp (int): The hit points of the character.
            shield (int): The shield points of the character.
            dodge_score (int): The dodge score of the character.
            ability_threshold (int): The threshold for using special abilities.
            special_name (str): The name of the special ability.
            special_desc (str): The description of the special ability.
            weapon (Weapon): The weapon the character uses.
        """
        self.name = name
        self.hp = hp
        self.shield = shield
        self.weapon = weapon
        self.dodge_score = dodge_score

        self.special_name = special_name
        self.special_desc = special_desc
        self.accuracy_penalty = 0
        self.countdown = 0
        self.ability_threshold = ability_threshold
        pass

    def attack(self):
        """
        Perform an attack using the character's weapon.

        Returns:
            int: The damage dealt, or 0 if the attack misses.
        """
        effective_accuracy = self.weapon.accuracy - self.accuracy_penalty
        self.countdown += 1
        if effective_accuracy <= 0:
            return 0
        else:
            return self.weapon.damage if randint(1, 100) <= effective_accuracy else 0

    def try_dodge(self) -> bool:
        """
        Attempt to dodge an incoming attack.

        Returns:
            bool: True if the dodge is successful, False otherwise.
        """
        return randint(1, 100) <= self.dodge_score

    def hit(self, received_damage: int) -> bool:
        """
        Process received damage and check if the character is defeated.

        Args:
            received_damage (int): The damage received.

        Returns:
            bool: True if the character is defeated, False otherwise.
        """
        if self.try_dodge():
            return True
        tmpdamage = received_damage - self.shield
        if tmpdamage > 0:
            self.hp -= tmpdamage
        return self.hp <= 0

class Berry_Ninja(Character):
    def __init__(self):
        """
        Initialize a Berry Ninja character with specific attributes and abilities.
        """
        super().__init__("Berry Ninja", 20, 5, 40, 2, "Berry Dash", "Dashing forward! Will dodge next attack.", Weapon("Berry", 4, 1, 60))
        self.dodge_next = False

    def try_dodge(self) -> bool:
        """
        Attempt to dodge an incoming attack with a special condition.

        Returns:
            bool: True if the dodge is successful, False otherwise.
        """
        if self.dodge_next:
            self.dodge_next = False
            return True
        else:
            return super().try_dodge()

    def use_special(self) -> bool:
        """
        Use the special ability if the countdown threshold is met.

        Returns:
            bool: True if the special ability is used, False otherwise.
        """
        if self.countdown < self.ability_threshold:
            return False
        else:
            self.countdown = 0
            self.dodge_next = True
            return True

class Sergeant_Broccoli(Character):
    def __init__(self):
        """
        Initialize a Sergeant Broccoli character with specific attributes and abilities.
        """
        super().__init__("Sergeant", 40, 10, 25, 3, "Shield Boost", "Weak spots identified! Next attack +50% damage!", Weapon("Broccoli Hammer", 5, 5, 70))
        self.damage_reduction = 1.0

    def hit(self, received_damage: int) -> bool:
        """
        Process received damage with a damage reduction factor.

        Args:
            received_damage (int): The damage received.

        Returns:
            bool: True if the character is defeated, False otherwise.
        """
        if self.try_dodge():
            return True

        tmpdamage = received_damage * self.damage_reduction - self.shield
        if tmpdamage > 0:
            self.hp -= tmpdamage
        return self.hp <= 0

    def use_special(self) -> bool:
        """
        Use the special ability if the countdown threshold is met.

        Returns:
            bool: True if the special ability is used, False otherwise.
        """
        if self.countdown < self.ability_threshold:
            return False
        else:
            self.countdown = 0
            self.damage_reduction = 0.5
            return True

class Captain_Carrot(Character):
    def __init__(self):
        """
        Initialize a Captain Carrot character with specific attributes and abilities.
        """
        super().__init__("Captain Carrot", 30, 5, 30, 3, "Enhanced Eyesight", "Weak spots identified! Next attack +50% damage!", Weapon("Carrot Sword", 5, 3, 90))
        self.next_attack_multiplier = 1.0

    def attack(self):
        """
        Perform an attack with a potential damage multiplier.

        Returns:
            int: The damage dealt, or 0 if the attack misses.
        """
        effective_accuracy = self.weapon.accuracy - self.accuracy_penalty
        self.countdown += 1
        if effective_accuracy <= 0:
            return 0
        else:
            if randint(1, 100) <= effective_accuracy:
                final_damage = int(self.weapon.damage * self.next_attack_multiplier)
                self.next_attack_multiplier = 1.0
                return final_damage
            else:
                return 0

    def use_special(self) -> bool:
        """
        Use the special ability if the countdown threshold is met.

        Returns:
            bool: True if the special ability is used, False otherwise.
        """
        if self.countdown < self.ability_threshold:
            return False
        else:
            self.countdown = 0
            self.next_attack_multiplier = 1.5
            return True
