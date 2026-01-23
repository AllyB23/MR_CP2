# MR 1st Random Password Generator
import random

def main():
        print("Welcome to the random Password Generator...")
        print("You are able to generate random passwords...")
        print("with the requirements you need!")
        choice = ("Would you like to continue or leave?")
        print("1. Continue to generate passwords")
        print("2. Leave")
        
        if choice == '1':
            requirements()
        elif choice == '2':
            return
        else:
            print("Please enter a valid value.")
        
def requirements():
    """How long does the password need to be: 
    Does the password need lowercase letters:
    Does the passeords need uppercase letters:
    Does the passwords need numbers letters:
    Possible passwords: """
    lower = ("Does the password need lower case letters(Y/N): ")
    upper = ("Does the password need upper case letters(Y/N): ")
    numbers = ("Does the password need numbers letter(Y/N): ")
    special_characters = ("Does the password need special characters letters(Y/N): ")

    while True:
        if lower == 'y':
            print("")
        elif lower == 'n':
            print("")
        else:
            break
    while True:
        if upper == 'y':
            print("")
        elif upper == 'n':
            print("")
        else:
            break
    while True:
        if numbers == 'y':
             print("")
        elif numbers == 'n':
            print("")
        else:
            break
    while True:
        if special_characters == 'y':
                print("")
        elif special_characters == 'n':
                print("")
        else:
            break

    pass
main()