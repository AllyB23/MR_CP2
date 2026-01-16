# MR 2nd Personal Library

books = {"The Hobbit by J.R.R Tolkein", "A Wrinkle in Time by Madeleine L'Engle", "Steelheart by Brandon Sanderson", "The Chroincles of Narnia: The horse and His Boy by C.S. Lewis", "The Guve by Lois Lowry", "Howl's Moving Castle by Diana Wynne Jones", "Artemis Fowl by Brandon Mull", "Fablehaven by Brandon Mull", "Inkheart by Cornelia Funke"}# I am using a main function for welcomin the user and saying instructions
def main():  # The main function is acting a sa lobby for the Personal Library  
    # This is welcoming the user and explaining what to do and how the Personal Library works
    print("Welcome to your Personal Library!")
    print("Your Personal Library is able to store your books and have the ability to View, add, remove, or search your library.")
    print("You may choose any of those options by entering the number that corresponds with the action.")
    print("1. View your personal Library")
    print("2. Add to your Personal Library")
    print("3. Remove from your personal Library")
    print("4. Search your Personal Library")
    print("5. Exit your Personal Library")

    choice = input("What action would you like to perform? ")


    if choice == "1":
        view()
    elif choice == "2":
        add()
    elif choice == "3":
        remove()
    elif choice == "4":
        search()
    elif choice == "5":
        print("Thank You, goodbye.")
    else:
        print("Invalid Choice, please try again.")
        main()

# These are the functions for the actions for the Personal Library
def view():
    print("\n Your books:")
    for book in books:
        print(f" - {book}")
    main()

def add():
    new_book = input("What is the Title of the book you want to add: ")
    author = input("Who is the book by: ")
    books.add(new_book)
    print(f" ' {new_book}' has been added!")
    main()

def remove():
    list = []
    #print("book choices" in a list)
    # Display all book items as a numbered list
    bookz = float(input("Enter the number of the item you would like to remove: "))
    print(f"You have removed {bookz} from your Personal Library.")
    print(f"This is your new list of books {bookz}.")
    main()

def search():
    print("1. Title")
    print("2. Author")
    search_by = float(input("What would you like to search by? "))

    # This is to perform the action that the user chooses
    if search_by == "1":
        auhtors_name = input("What is the authors name: ").isalpha()
        print(f"")
    elif search_by == "2":
        title_of_book = input("What is the title of the book: ")
    else:
        print("Please enter a valid number. ")

main()