# MR 1st Random Password Generator
import random

def main():
    while True:
        print("Welcome to the random Password Generator...")
        print("You are able to generate random passwords...")
        print("with the requirements you need!")
        choice = ("Would you like to continue or leave?")
        print("1. Continue to generate passwords")
        print("2. Leave")
        
        if choice == '1':
            requirements()
        elif choice == '2':
            break
        else:
            print("Please enter a valid value.")
        pass
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
        elif lower == 'n':
        else:
            break
        if upper == 'y':
        elif upper == 'n':
        else:
            break
        if numbers == 'y':
        elif numbers == 'n':
        else:
            break
        if special_characters == 'y':
        elif special_characters == 'n':
        else:
            break

    pass
