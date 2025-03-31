from random import randint

from weapon import Weapon

class Character :
    def __init__(self, name:str, hp:int, shield:int, dodge_score:int, ability_threshold:int, special_name:str, special_desc:str, weapon : Weapon) :
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

    def attack(self) :
        effective_accuracy = self.weapon.accuracy - self.accuracy_penalty
        self.countdown += 1
        if effective_accuracy <= 0 :
            return 0
        else :
            return self.weapon.damage if randint(1,100) <= effective_accuracy else 0

    def try_dodge(self) -> bool :
        return randint(1,100) <= self.dodge_score

    def hit(self, received_damage:int) -> bool :
        if self.try_dodge() :
            return True
        tmpdamage = received_damage - self.shield
        if tmpdamage > 0 :
            self.hp -= tmpdamage
        return self.hp <= 0

class Berry_Ninja(Character) :
    def __init__(self) :
        super().__init__("Berry Ninja", 20, 5, 40, 2, "Berry Dash", "Dashing forward! Will dodge next attack.", Weapon("Berry", 4, 1, 60))
        self.dodge_next = False

    def try_dodge(self) -> bool :
        if self.dodge_next : 
            self.dodge_next = False
            return True
        else : 
            return super().try_dodge()

    def use_special(self) -> bool:
        """return if the special has been used"""
        if self.countdown < self.ability_threshold :
            return False
        else :
            self.countdown = 0
            self.dodge_next = True
            return True

class Sergeant_Broccoli(Character) :
    def __init__(self) :
        super().__init__("Sergeant", 40, 10, 25, 3,"Shield Boost","Weak spots identified! Next attack +50% damage!", Weapon("Broccoli Hammer", 5, 5,70))
        self.damage_reduction = 1.0

    def hit(self, received_damage:int) -> bool :
        if self.try_dodge() :
            return True

        tmpdamage = received_damage * self.damage_reduction - self.shield
        if tmpdamage > 0 :
            self.hp -= tmpdamage
        return self.hp <= 0

    def use_special(self) -> bool:
        """return if the special has been used"""
        if self.countdown < self.ability_threshold :
            return False
        else :
            self.countdown = 0
            self.damage_reduction = 0.5
            return True

class Captain_Carrot(Character) :
    def __init__(self) :
        super().__init__("Captain Carrot", 30, 5, 30, 3,"Enhanced Eyesight", "Weak spots identified! Next attack +50% damage!", Weapon("Carrot Sword",5,3,90))
        self.next_attack_multiplier = 1.0

    def attack(self) :
        effective_accuracy = self.weapon.accuracy - self.accuracy_penalty
        self.countdown += 1
        if effective_accuracy <= 0 :
            return 0
        else :
            if randint(1,100) <= effective_accuracy :
                final_damage = int(self.weapon.damage * self.next_attack_multiplier)
                self.next_attack_multiplier = 1.0
                return final_damage
            else :
                return 0

    def use_special(self) -> bool:
        """return if the special has been used"""
        if self.countdown < self.ability_threshold :
            return False
        else :
            self.countdown = 0
            self.next_attack_multiplier = 1.5
            return True
