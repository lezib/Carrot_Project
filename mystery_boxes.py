
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

    def open(self, player, enemy):
        # Randomly choose an item from the box
        item = random.choice(self.items)
        print(f"\n{player.name} opened the mystery box and found a {item.name}!")

        # If the item is a debuff, we apply it to the enemy (just an example)
        if item.is_debuff:
            print(f"{enemy.name} is affected by {item.name}, reducing their attack!")
            item.use(enemy)  # Apply the debuff to the enemy
        else:
            # Give the item to the player, let them equip or use it
            player.inventory.equip_weapon(item) if item.item_type == "weapon" else \
                player.inventory.equip_shield(item) if item.item_type == "shield" else \
                player.inventory.equip_debuff(item) if item.item_type == "debuff" else \
                player.inventory.healing_item = item

        # Show updated inventory after using the mystery box
        player.inventory.show_inventory()

# Update the combat function to include the mystery box option
def combat(player, enemy):
    while player.is_alive() and enemy.is_alive():
        print(f"\n{player.name} vs {enemy.name} - Health: {player.hp} / {enemy.hp}")
        print("1. Attack  2. Use Item  3. Open Mystery Box")
        choice = input("What would you like to do? ")

        if choice == "1":
            player.attack_enemy(enemy)
        elif choice == "2":
            player.show_inventory()
            item_choice = int(input("Choose an item to use (by index): "))
            player.use_item(player.inventory.items[item_choice])  # Assume items are displayed as a list
        elif choice == "3":
            mystery_box = MysteryBox()  # Create a mystery box instance
            mystery_box.open(player, enemy)  # Open the mystery box
        else:
            print("Invalid choice!")
        
        # Enemy's turn (for simplicity, let's assume they always attack)
        if enemy.is_alive():
            enemy.attack_player(player)
        else:
            print(f"{enemy.name} has been defeated!")

    if player.is_alive():
        print(f"{player.name} wins!")
    else:
        print(f"{player.name} has been defeated.")

