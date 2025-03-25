import random

# Weapon Class
class Weapon:
    def __init__(self, name, damage, accuracy, special):
        self.name = name
        self.damage = damage
        self.accuracy = accuracy  # Percentage chance to hit
        self.special = special  # Special ability description
    
    def attack(self):
        if random.randint(1, 100) <= self.accuracy:
            return self.damage
        else:
            return 0  # Missed attack

# Enemy (Boss) Class
class Enemy:
    def __init__(self, name, hp, shield, damage, special):
        self.name = name
        self.hp = hp
        self.shield = shield
        self.damage = damage
        self.special = special
        self.turn_counter = 0

    def attack(self):
        if random.randint(1, 100) <= 90:  # 10% miss chance
            if self.special == "Melty Mayhem":
                # Apply dodge & double strike logic
                damage = self.damage
                if random.randint(1, 100) <= 50:
                    damage *= 2
                    print(f"{self.name} attacks twice!")
                return damage
            return self.damage
        return 0

    def apply_special(self):
        if self.special == "Melty Mayhem":
            if self.turn_counter % 2 == 0:
                self.hp += 10
                print(f"{self.name} heals 10 HP from Melty Mayhem!")

# Player Class
class Player:
    def __init__(self, name, hp, shield, weapon, special):
        self.name = name
        self.hp = hp
        self.shield = shield
        self.weapon = weapon
        self.special = special
        self.cooldown = 0
        self.accuracy_penalty = 0
        
        # New additions to player class 
        self.dodge_next = False  # For Berry Ninja
        self.damage_reduction = 1.0  # For Sergeant Broccoli
        self.next_attack_multiplier = 1.0  # For Captain Carrot
        self.cooldown = 0

    def attack(self):
        effective_accuracy = self.weapon.accuracy - self.accuracy_penalty
        if random.randint(1, 100) <= max(0, effective_accuracy):
            return self.weapon.damage
        return 0
    
    #Update the use_special function
    def use_special(self):
        if self.cooldown > 0:
            print(f"Ability on cooldown! ({self.cooldown} turns left)")
            return False
    
        if self.special == "Enhanced Eyesight":
            self.next_attack_multiplier = 1.5
            print("Weak spots identified! Next attack +50% damage!")
        elif self.special == "Shield Boost":
            self.shield += 20
            self.damage_reduction = 0.5  # 50% less damage
            print("Shield boosted! Damage reduced for 2 turns.")
        elif self.special == "Berry Dash":
            self.dodge_next = True
            print("Dashing forward! Will dodge next attack.")
    
        self.cooldown = 3
        return True
    
    ''' previous code for the use_special
    def use_special(self):
        if self.special == "Enhanced Eyesight":
            return int(self.weapon.damage * 1.5)
        elif self.special == "Shield Boost":
            self.shield += 20
            print("Shield boosted by 20! Reduced damage for 2 turns.")
            return 0
        elif self.special == "Berry Dash":
            print("Berry Dash activated! Dodging next attack.")
            return 15  # Extra damage
        return 0
    '''

# Mystery Box System

def open_mystery_box():
    mystery_outcomes = [
        ("Better Weapon", Weapon("Green Bean Launcher", 30, 65, "High Power")),
        ("Weaker Weapon", Weapon("Celery Stick", 10, 95, "Poke")),
        ("Boss Advantage Weapon", Weapon("Spinach Spear", 20, 80, "Bonus vs Fries Serpent")),
        ("Buff - Extra Health", "extra_health"),
        ("Buff - Shield Boost", "shield_boost"),
        ("Buff - Accuracy Boost", "accuracy_boost"),
        ("Debuff - Lose Health", "lose_health"),
        ("Debuff - Lower Damage", "lower_damage")
    ]
    choice = random.choice(mystery_outcomes)
    print(f"You opened a mystery box: {choice[0]}")
    return choice[1]

# Game Combat System

def combat(player, enemy):
    turn = 1
    dodge_next = False
    while player.hp > 0 and enemy.hp > 0:
        print(f"\n--- Turn {turn} ---")

        # Apply any special effects
        enemy.apply_special()

        # Player Turn
        action = random.choice(['a', 's'])
        print(f"[AUTO] Player chose: {action.upper()}")
        if action == 'a':
            damage = player.attack()
            if damage > 0:
                print(f"You hit {enemy.name} for {damage} damage!")
                if enemy.shield > 0:
                    absorbed = min(damage, enemy.shield)
                    enemy.shield -= absorbed
                    damage -= absorbed
                enemy.hp -= damage
            else:
                print("You missed!")
        elif action == 's' and player.cooldown == 0:
            result = player.use_special()
            if player.special == "Berry Dash":
                dodge_next = True
                enemy.hp -= result
            elif player.special == "Enhanced Eyesight":
                enemy.hp -= result
            player.cooldown = 3

        # Enemy Turn
        if enemy.hp > 0:
            if dodge_next:
                print("You dodged the attack!")
                dodge_next = False
            else:
                dmg = enemy.attack()
                print(f"{enemy.name} attacks for {dmg} damage!")
                if player.shield > 0:
                    absorbed = min(dmg, player.shield)
                    player.shield -= absorbed
                    dmg -= absorbed
                player.hp -= dmg

        if player.cooldown > 0:
            player.cooldown -= 1
        enemy.turn_counter += 1

        if enemy.hp <= 0:
            print(f"You defeated {enemy.name}!")
            break
        if player.hp <= 0:
            print("You were defeated! Game Over.")
            break

        turn += 1

# Game Setup
characters = [
    Player("Captain Carrot", 100, 30, Weapon("Carrot Daggers", 20, 85, "Sharp"), "Enhanced Eyesight"),
    Player("Sergeant Broccoli", 100, 30, Weapon("Broccoli Hammer", 15, 90, "Heavy Hit"), "Shield Boost"),
    Player("Berry Ninja", 100, 30, Weapon("Berry Bombs", 25, 75, "Explode"), "Berry Dash")
]

# Randomly select a hero
player = random.choice(characters)
print(f"You are playing as {player.name} with weapon {player.weapon.name}!")

# Enemy List
enemy_list = [
    Enemy("Junky Dummy", 20, 0, 0, None),
    Enemy("Snickers Fiend", 50, 0, 10, None),
    Enemy("Mountain Dew Slime", 80, 15, 15, "Foam Release"),
    Enemy("Fries Serpent", 100, 20, 20, "Grease Wave"),
    Enemy("Donut Juggernaut", 120, 25, 25, "Sugar Shock"),
    Enemy("Lord Pizza Supreme", 150, 30, 30, "Melty Mayhem")
]

# Game Loop
for enemy in enemy_list:
    print(f"\n--- Enemy Encounter: {enemy.name} ---")
    
    # Mystery box phase (after level 1)
    if enemy.name != "Junky Dummy":
        if random.choice([True, False]):
            reward = open_mystery_box()
            if isinstance(reward, Weapon):
                player.weapon = reward
                print(f"New weapon equipped: {player.weapon.name}")
            elif reward == "extra_health":
                player.hp += 10
                print("Gained 10 HP!")
            elif reward == "shield_boost":
                player.shield += 15
                print("Gained 15 Shield!")
            elif reward == "accuracy_boost":
                player.weapon.accuracy += 20
                print("Increased accuracy by 20%!")
            elif reward == "lose_health":
                player.hp -= 10
                print("Lost 10 HP!")
            elif reward == "lower_damage":
                player.weapon.damage = max(5, player.weapon.damage - 5)
                print("Weapon damage reduced by 5!")
    
    combat(player, enemy)
    if player.hp <= 0:
        break

print("Game Over! Thanks for playing!")
