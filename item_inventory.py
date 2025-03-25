'''
Define an inventory that will store the player's item.
Each item has 3 attributes: name, type (weapon, buff, debuff, healing, shield), and effect
'''

class Item:
    def __init__(self, name, item_type, effect, is_debuff=False):
        self.name = name
        self.item_type = item_type  # e.g., "weapon", "healing", "buff", "shield", "debuff"
        self.effect = effect  # e.g., +20 HP, +10 Attack, +Shield, or damage dealt
        self.is_debuff = is_debuff  # True if it's a debuff, False if it's a buff or other item

    def use(self, player):
        #Use the item and apply its effect to the player.
        if self.is_debuff:
            if self.item_type == "debuff":
                player.attack -= self.effect
                print(f"{player.name} used {self.name} and lost {self.effect} Attack!")
        elif self.item_type == "healing":
            player.hp += self.effect
            print(f"{player.name} used {self.name} and gained {self.effect} HP!")
        elif self.item_type == "buff":
            player.attack += self.effect
            print(f"{player.name} used {self.name} and gained +{self.effect} Attack!")
        elif self.item_type == "shield":
            player.shield += self.effect
            print(f"{player.name} used {self.name} and gained +{self.effect} Shield!")
        elif self.item_type == "weapon":
            player.weapon = self  # Equip the weapon
            print(f"{player.name} equipped {self.name}!")

class Inventory:
    def __init__(self):
        self.weapon = None  # Player can only have one weapon at a time
        self.shield = None  # Player can equip one shield if they need to
        self.healing_item = None  # Single healing item
        self.debuff_item = None  # Player can hold a debuff item

    def equip_weapon(self, item):
        #Equip a weapon to the player.
        if item.item_type == "weapon":
            self.weapon = item
            print(f"{item.name} equipped!")
        else:
            print(f"{item.name} is not a weapon and cannot be equipped.")

    def equip_shield(self, item):
        #Equip a shield to the player.
        if item.item_type == "shield":
            self.shield = item
            print(f"{item.name} equipped!")
        else:
            print(f"{item.name} is not a shield and cannot be equipped.")

    def equip_debuff(self, item):
        #Equip a debuff item to the player.
        if item.item_type == "debuff":
            self.debuff_item = item
            print(f"{item.name} equipped as a debuff!")
        else:
            print(f"{item.name} is not a debuff and cannot be equipped.")

    def drop_weapon(self):
        #Drop the equipped weapon.
        if self.weapon:
            print(f"Dropped {self.weapon.name}.")
            self.weapon = None
        else:
            print("No weapon to drop.")

    def drop_shield(self):
        #Drop the equipped shield.
        if self.shield:
            print(f"Dropped {self.shield.name}.")
            self.shield = None
        else:
            print("No shield to drop.")

    def drop_debuff(self):
        #Drop the equipped debuff.
        if self.debuff_item:
            print(f"Dropped {self.debuff_item.name}.")
            self.debuff_item = None
        else:
            print("No debuff to drop.")

    def use_weapon(self, player):
        #Use the equipped weapon.
        if self.weapon:
            self.weapon.use(player)
        else:
            print("No weapon equipped!")

    def use_shield(self, player):
        #Use the equipped shield (if necessary, adds to player's shield points).
        if self.shield:
            self.shield.use(player)
        else:
            print("No shield equipped!")

    def use_debuff(self, player):
        #Use the debuff item (apply negative effect).
        if self.debuff_item:
            self.debuff_item.use(player)
        else:
            print("No debuff equipped!")

    def use_healing_item(self, player):
        #Use the healing item (if equipped).
        if self.healing_item:
            self.healing_item.use(player)
            self.healing_item = None  # Remove the item after use
        else:
            print("No healing item equipped!")

    def show_inventory(self):
        #Show the equipped items.
        if self.weapon:
            print(f"Equipped Weapon: {self.weapon.name}")
        else:
            print("No weapon equipped.")

        if self.shield:
            print(f"Equipped Shield: {self.shield.name}")
        else:
            print("No shield equipped.")
        
        if self.healing_item:
            print(f"Equipped Healing Item: {self.healing_item.name}")
        else:
            print("No healing item equipped.")

        if self.debuff_item:
            print(f"Equipped Debuff Item: {self.debuff_item.name}")
        else:
            print("No debuff item equipped.")
