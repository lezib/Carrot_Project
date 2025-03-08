# inventory_system.py

class Item:
    def __init__(self, name, item_type, effect):
        self.name = name
        self.item_type = item_type  # e.g., "weapon", "healing", "buff", "shield"
        self.effect = effect  # e.g., +20 HP, +10 Attack

    def use(self, player):
        # Apply the item's effect to the player
        if self.item_type == "healing":
            player.health += self.effect
            print(f"{player.name} used {self.name} and gained {self.effect} HP!")
        elif self.item_type == "buff":
            player.attack += self.effect
            print(f"{player.name} used {self.name} and gained +{self.effect} Attack!")
        elif self.item_type == "shield":
            player.shield += self.effect
            print(f"{player.name} used {self.name} and gained +{self.effect} Shield!")
        elif self.item_type == "weapon":
            player.weapon = self
            print(f"{player.name} equipped {self.name}!")

class Inventory:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.items = []

    def add_item(self, item):
        if len(self.items) < self.capacity:
            self.items.append(item)
            print(f"{item.name} added to inventory.")
        else:
            print("Inventory is full! Drop an item to make space.")

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            print(f"{item.name} removed from inventory.")
        else:
            print(f"{item.name} not found in inventory.")

    def use_item(self, item, player):
        if item in self.items:
            item.use(player)
            self.remove_item(item)  # Remove the item after use
        else:
            print(f"{item.name} not found in inventory.")

    def show_inventory(self):
        print("Inventory:")
        for item in self.items:
            print(f"- {item.name} ({item.item_type}): {item.effect}")

# Define some items
carrot_daggers = Item("Carrot Daggers", "weapon", 20)
banana_smoothie = Item("Banana Smoothie", "healing", 20)
spinach_power = Item("Spinach Power", "buff", 10)
kale_armor = Item("Kale Armor", "shield", 30)