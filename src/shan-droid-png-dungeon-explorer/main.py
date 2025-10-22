import random
import time

class DungeonExplorer:
    def __init__(self):
        self.player_hp = 100
        self.player_gold = 0
        self.potions = 2
        self.rooms_explored = 0
        
    def print_slow(self, text, delay=0.03):
        """Print text with a typewriter effect"""
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()
    
    def show_stats(self):
        """Display player statistics"""
        print("\n" + "="*40)
        print(f"❤️  HP: {self.player_hp} | 💰 Gold: {self.player_gold} | 🧪 Potions: {self.potions}")
        print("="*40 + "\n")
    
    def use_potion(self):
        """Use a health potion"""
        if self.potions > 0:
            heal = random.randint(20, 40)
            self.player_hp = min(100, self.player_hp + heal)
            self.potions -= 1
            self.print_slow(f"You drink a potion and restore {heal} HP!")
            return True
        else:
            print("You don't have any potions!")
            return False
    
    def combat(self, enemy_name, enemy_hp, enemy_damage):
        """Combat system"""
        self.print_slow(f"\n⚔️  A {enemy_name} appears! (HP: {enemy_hp})")
        
        while enemy_hp > 0 and self.player_hp > 0:
            print("\n1. Attack")
            print("2. Use Potion")
            print("3. Try to flee")
            
            choice = input("\nWhat do you do? ").strip()
            
            if choice == "1":
                damage = random.randint(15, 30)
                enemy_hp -= damage
                self.print_slow(f"You strike for {damage} damage!")
                
                if enemy_hp > 0:
                    enemy_dmg = random.randint(enemy_damage - 5, enemy_damage + 5)
                    self.player_hp -= enemy_dmg
                    self.print_slow(f"The {enemy_name} hits you for {enemy_dmg} damage!")
            
            elif choice == "2":
                if self.use_potion():
                    enemy_dmg = random.randint(enemy_damage - 5, enemy_damage + 5)
                    self.player_hp -= enemy_dmg
                    self.print_slow(f"The {enemy_name} hits you for {enemy_dmg} damage!")
            
            elif choice == "3":
                if random.random() < 0.4:
                    self.print_slow("You successfully fled!")
                    return False
                else:
                    self.print_slow("You failed to escape!")
                    enemy_dmg = random.randint(enemy_damage - 5, enemy_damage + 5)
                    self.player_hp -= enemy_dmg
                    self.print_slow(f"The {enemy_name} hits you for {enemy_dmg} damage!")
            
            else:
                print("Invalid choice!")
        
        if self.player_hp > 0:
            gold = random.randint(10, 30)
            self.player_gold += gold
            self.print_slow(f"\n🎉 Victory! You found {gold} gold!")
            return True
        
        return False
    
    def explore_room(self):
        """Explore a random room"""
        self.rooms_explored += 1
        self.show_stats()
        
        events = ['enemy', 'treasure', 'potion', 'trap', 'empty']
        event = random.choice(events)
        
        if event == 'enemy':
            enemies = [
                ("Goblin", 30, 10),
                ("Skeleton", 40, 12),
                ("Dark Elf", 50, 15),
                ("Orc", 60, 18)
            ]
            enemy = random.choice(enemies)
            if not self.combat(enemy[0], enemy[1], enemy[2]):
                return False
        
        elif event == 'treasure':
            gold = random.randint(20, 50)
            self.player_gold += gold
            self.print_slow(f"💰 You found a treasure chest with {gold} gold!")
        
        elif event == 'potion':
            self.potions += 1
            self.print_slow("🧪 You found a health potion!")
        
        elif event == 'trap':
            damage = random.randint(10, 20)
            self.player_hp -= damage
            self.print_slow(f"⚠️  You triggered a trap and lost {damage} HP!")
        
        else:
            self.print_slow("The room is empty. Nothing of interest here.")
        
        return self.player_hp > 0
    
    def play(self):
        """Main game loop"""
        self.print_slow("🏰 Welcome to Dungeon Explorer! 🏰")
        self.print_slow("Explore the dungeon, fight monsters, and collect gold!")
        input("\nPress Enter to begin your adventure...")
        
        while self.player_hp > 0:
            print("\n" + "="*40)
            print("What would you like to do?")
            print("1. Explore next room")
            print("2. Check stats")
            print("3. Use potion")
            print("4. Exit dungeon")
            print("="*40)
            
            choice = input("\nYour choice: ").strip()
            
            if choice == "1":
                if not self.explore_room():
                    break
            
            elif choice == "2":
                self.show_stats()
            
            elif choice == "3":
                self.use_potion()
            
            elif choice == "4":
                self.print_slow("\nYou exit the dungeon safely.")
                break
            
            else:
                print("Invalid choice! Try again.")
        
        print("\n" + "="*40)
        print("🎮 GAME OVER 🎮")
        print(f"Rooms explored: {self.rooms_explored}")
        print(f"Gold collected: {self.player_gold}")
        print(f"Final HP: {max(0, self.player_hp)}")
        print("="*40)

# Start the game
if __name__ == "__main__":
    game = DungeonExplorer()
    game.play()