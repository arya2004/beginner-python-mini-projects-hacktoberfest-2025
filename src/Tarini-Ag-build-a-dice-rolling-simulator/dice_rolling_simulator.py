import random

def roll_dice(num_dice=1, num_sides=6):
    """
    Roll one or more dice with specified number of sides.
    
    Args:
        num_dice (int): Number of dice to roll (default: 1)
        num_sides (int): Number of sides on each die (default: 6)
    
    Returns:
        list: Results of each die roll
    """
    results = []
    for _ in range(num_dice):
        roll = random.randint(1, num_sides)
        results.append(roll)
    return results

def display_dice(results):
    """
    Display the results of dice rolls in a formatted way.
    
    Args:
        results (list): List of dice roll results
    """
    print("\n" + "="*40)
    print("🎲 DICE ROLL RESULTS 🎲")
    print("="*40)
    for i, result in enumerate(results, 1):
        print(f"Die {i}: {result}")
    print(f"\nTotal: {sum(results)}")
    print("="*40 + "\n")

def main():
    """
    Main function to run the dice rolling simulator.
    """
    print("\n🎲 Welcome to the Dice Rolling Simulator! 🎲\n")
    
    while True:
        try:
            # Get user input for number of dice
            num_dice = int(input("How many dice would you like to roll? (1-10): "))
            if num_dice < 1 or num_dice > 10:
                print("Please enter a number between 1 and 10.")
                continue
            
            # Get user input for number of sides
            num_sides = int(input("How many sides should each die have? (2-20): "))
            if num_sides < 2 or num_sides > 20:
                print("Please enter a number between 2 and 20.")
                continue
            
            # Roll the dice
            results = roll_dice(num_dice, num_sides)
            
            # Display results
            display_dice(results)
            
            # Ask if user wants to roll again
            again = input("Would you like to roll again? (yes/no): ").lower()
            if again not in ['yes', 'y']:
                print("\nThanks for playing! Goodbye! 👋\n")
                break
                
        except ValueError:
            print("\nInvalid input! Please enter a valid number.\n")
        except KeyboardInterrupt:
            print("\n\nExiting the program. Goodbye! 👋\n")
            break

if __name__ == "__main__":
    main()
