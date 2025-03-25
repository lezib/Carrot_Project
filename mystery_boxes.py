
import random
from item_inventory import Item

'''
This is the mystery box system. 

The mystery box will contain a random item, which could be a weapon, shield, debuff, or healing item.

When the player opens the mystery box, they will randomly receive an item. They can then equip or use it as part of their inventory.

Each item will have an effect, and the player can choose to equip it or use it in the next turn.
'''

# Define the possible items for the mystery box
class MysteryBox:
    def __init__(self):
        self.items = [
            Item(name="Sword of Power", item_type="weapon", effect=30),  # Weapon item
            Item(name="Healing Potion", item_type="healing", effect=20),  # Healing item
            Item(name="Shield of Fortitude", item_type="shield", effect=25),  # Shield item
            Item(name="Weakening Curse", item_type="debuff", effect=10, is_debuff=True)  # Debuff item
        ]

# Opening the mystery box 
def open(self, player):
    # Possible outcomes (aligned with your game design)
    possible_items = [
        # Weapons (name, type, effect)
        ("Green Bean Launcher", "weapon", 30),
        ("Celery Stick", "weapon", 10),
        ("Spinach Spear", "weapon", 20),
        # Buffs/Debuffs (name, type, effect, is_debuff)
        ("Vitamin Boost", "healing", 20),
        ("Kale Shield", "shield", 25),
        ("Sugar Crash", "debuff", -10, True)
    ]
    
    # Random selection with weighting (60% weapon, 40% buff/debuff)
    if random.random() < 0.6:
        item_type = "weapon"
        items = [i for i in possible_items if i[1] == "weapon"]
    else:
        item_type = random.choice(["healing", "shield", "debuff"])
        items = [i for i in possible_items if i[1] == item_type]
    
    selected = random.choice(items)
    item = Item(*selected)  # Create Item object
    
    print(f"\nYou found: {item.name}!")
    
    # Handle item based on type
    if item.item_type == "weapon":
        print(f"Equip this weapon? (Damage: {item.effect})")
        choice = input("(y/n): ").lower()
        if choice == 'y':
            player.weapon = item
    else:
        item.use(player)  # Apply effect immediately for non-weapons
    
    # For final level only (preview option)
    if player.level == 6:
        print("\nFinal level bonus: You can preview the item!")
        print(f"Effect: {item.effect}")
