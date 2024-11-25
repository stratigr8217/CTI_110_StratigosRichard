#Richard Stratigos
#11/24/2024
#P5HW
#Character creation game

import random

# Value-returning function to create a character

def create_character():
    print("\n🛡️ Create a New Character 🛡️")
    name = input("Enter character's name: ")
    health = int(input("Enter character's health (e.g., 100): "))
    attack_points = int(input("Enter character's attack points (e.g., 20): "))
    character = {
        "Name": name,
        "Health": health,
        "Attack Points": attack_points,
    }
    print(f"\n✨ Character '{name}' created successfully!")
    return character

# Non-value returning function to display all characters

def display_characters(character_list):
    if not character_list:
        print("\n⚠️ No characters to display.")
        return
    print("\n👥 List of Characters:")
    for idx, character in enumerate(character_list, 1):
        print(f"\nCharacter {idx}:")
        for key, value in character.items():
            print(f"  {key}: {value}")

# Function to handle character battles

def battle(character1, character2):
    print(f"\n⚔️ Battle: {character1['Name']} vs {character2['Name']} ⚔️")
    attacker = character1
    defender = character2
    while character1["Health"] > 0 and character2["Health"] > 0:
        damage = random.randint(0, attacker["Attack Points"])
        defender["Health"] -= damage
        print(f"{attacker['Name']} attacks {defender['Name']} for {damage} damage!")
        print(f"{defender['Name']}'s remaining health: {defender['Health']}")

        if defender["Health"] <= 0:
            print(f"🏆 {attacker['Name']} wins the battle!")
            break

        # Swap roles
        attacker, defender = defender, attacker

# Main function

def main():
    characters = []
    while True:
        print("\n=== Character Creation Game Menu ===")
        print("1. Create a character")
        print("2. Display all characters")
        print("3. Battle between characters")
        print("4. Exit the game")
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            character = create_character()
            characters.append(character)
        elif choice == "2":
            display_characters(characters)
        elif choice == "3":
            if len(characters) < 2:
                print("\n⚠️ At least two characters are required for a battle.")
            else:
                print("\nChoose two characters to battle:")
                display_characters(characters)
                idx1 = int(input("Enter the number of the first character: ")) - 1
                idx2 = int(input("Enter the number of the second character: ")) - 1
                if idx1 == idx2 or idx1 < 0 or idx2 < 0 or idx1 >= len(characters) or idx2 >= len(characters):
                    print("\n⚠️ Invalid selection.")
                else:
                    battle(characters[idx1], characters[idx2])
                    # Remove characters with no health
                    characters = [c for c in characters if c["Health"] > 0]
        elif choice == "4":
            print("\n👋 Thanks for playing! Goodbye!")
            break
        else:
            print("\n⚠️ Invalid option. Please try again.")

# Run the main function
if __name__ == "__main__":
    main()
