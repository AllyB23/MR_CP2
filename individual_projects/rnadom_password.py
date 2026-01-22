# MR 1st Random Password Generator
import random

def main():
    while True:
        print("Welcome to the random Password Generator...")
        print("You are able to generate random passwords...")
        print("with the requirements you need!")
        print("Would you like to continue or leave?")
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
    pass
