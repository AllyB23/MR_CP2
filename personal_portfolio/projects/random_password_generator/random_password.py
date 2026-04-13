# MR 1st Random Password Generator
import random
import string

def main():
        
        while True:
            print("Welcome to the random Password Generator...")
            print("You are able to generate random passwords...")
            print("with the requirements you need!")
            print("1. Continue to generate passwords")
            print("2. Leave")

            choice = input("What would you like to do? ")        

            if choice == '1':
                generate_passwords_menu()
            elif choice == '2':
                break
            else:
                print("Please enter a valid value. Please type 1 or 2.")
        
def requirements():
    """How long does the password need to be: 
    Does the password need lowercase letters:
    Does the passeords need uppercase letters:
    Does the passwords need numbers letters:
    Possible passwords: """
    lower = input("Does the password need lower case letters(Y/N): ")
    upper = input("Does the password need upper case letters(Y/N): ")
    numbers = input("Does the password need numbers letter(Y/N): ")
    special_characters = input("Does the password need special characters letters(Y/N): ")

def get_boolean_input(prompt):
    """Helper function to validate Y/N inputs from the user."""
    while True:
        response = input(prompt).lower()
        if response == 'y':
            return True
        if response == 'n':
            return False
        print("Please enter 'Y' for Yes or 'N' for No.")

def assemble_password(length, char_pool):
    """Assembles a single random password from the character pool."""
    password = ""
    for _ in range(length):
        password += random.choice(char_pool)
    return password

def generate_passwords_menu():
    """Handles the password requirements and displays 4 results."""
    # Step 1: Get password length
    try:
        length = int(input("How long does the password need to be: "))
    except ValueError:
        print("Error: Length must be a number.")
        return

    # Step 2: Get character requirements
    use_lower = get_boolean_input("Does the password need lowercase letters (Y/N): ")
    use_upper = get_boolean_input("Does the password need uppercase letters (Y/N): ")
    use_numbers = get_boolean_input("Does the password need numbers (Y/N): ")
    use_special = get_boolean_input("Does the password need special characters (Y/N): ")

    # Step 3: Define character pools manually (no string module/ASCII art)
    char_pool = ""
    if use_lower:
        char_pool += "abcdefghijklmnopqrstuvwxyz"
    if use_upper:
        char_pool += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if use_numbers:
        char_pool += "0123456789"
    if use_special:
        char_pool += "!@#$%^&*()-_=+[]{}|;:,.<>?"

    # Check if the pool is empty
    if not char_pool:
        print("Error: You must select at least one character type.")
        return

    # Step 4: Generate 4 possible passwords
    print("\nPossible Passwords:")
    for _ in range(4):
        print(assemble_password(length, char_pool))

main()