
import random
from item_inventory import Item

'''
This is the mystery box system. 

There are two mystery boxes: one will contain weapons, the other will contain buffs and debuffs. 

When the player opens the mystery box, they will randomly receive an item. They can then equip or use it as part of their inventory.

Each item will have an effect, and the player can choose to equip it or use it in the next turn.
'''
# This is the weapon box
class WeaponBox:
    #Handles weapon-specific mystery boxes
    def __init__(self):
        self.weapons = [
            Item("Green Bean Launcher", "weapon", 30),
            Item("Celery Stick", "weapon", 10), 
            Item("Spinach Spear", "weapon", 20),
            Item("Carrot Daggers", "weapon", 20), 
            Item("Broccoli Hammer", "weapon", 15),
            Item("Berry Bombs", "weapon", 25)
        ]

    def open(self, player):
        weapon = random.choice(self.weapons)
        print(f"\n=== WEAPON BOX ===")
        print(f"Found: {weapon.name} (Damage: {weapon.effect})")
        
        choice = input("Equip? (y/n): ").lower()
        if choice == 'y':
            player.weapon = weapon
            print(f"Equipped {weapon.name}!")
        else:
            print("Left the weapon in the box.")

#This is the buff/debuff box
class BuffDebuffBox:
    """Handles buff/debuff mystery boxes""" 
    def __init__(self):
        self.items = [
            Item("Vitamin Boost", "healing", 20),
            Item("Kale Shield", "shield", 25),
            Item("Sugar Crash", "debuff", -10, True),
            # From combat.py's buff/debuffs:
            Item("Health Boost", "healing", 15), 
            Item("Shield Charge", "shield", 20),
            Item("Accuracy Debuff", "debuff", -15, True)
        ]

    def open(self, player):
        item = random.choice(self.items)
        print(f"\n=== BUFF/DEBUFF BOX ===")
        print(f"Found: {item.name}")
        
        if item.item_type == "debuff":
            print(f"WARNING: This is a debuff! (Effect: {item.effect})")
            input("Press Enter to continue...")
        
        item.use(player)  # Auto-applies effect