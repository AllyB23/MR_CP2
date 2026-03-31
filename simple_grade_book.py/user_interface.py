# MR 1st Simple Grade Book User Interface
# import module aliases
from classes import Student
from


def main():
    while True:
        print("==============SIMPLE GRADE BOOK===============")
        print("Welcome to your Simple Grade book...")
        print("Here you can input grades and student names to keep track of your class grades...")
        print("This program allows you to search up a student and add students as you please...")
        print("You can input then with their student ID if they have one or you can serach up by their first and last name...")
        print("You will be able to input their grades in percentage form and the program will give you their letter grade...")

        print("1. Add student")
        print("2. View Students")
        print("3. leave")

        choice = input("What would you like to do? ")

        if choice == '1':
            pass
        elif choice == '2':
            pass
        elif choice == '3':
            pass
        else:
            return
        print("Please enter a valid choice")

main()
