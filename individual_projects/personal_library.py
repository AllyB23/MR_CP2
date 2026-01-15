# MR 2nd Personal Library

def main():
    # This is welcoming the user and explaining what to do and how the Personal Library works
    print("Welcome to your Personal Library!")
    print("Your Personal Library is able to store your books and have the ability to View, add, remove, or search your library.")
    print("You may choose any of those options by entering the number that corresponds with the action.")
    print("1. View your personal Library")
    print("2. Add to your Personal Library")
    print("3. Remove from your personal Library")
    print("4. Search your Personal Library")
    print("5. Exit your Personal Library")

    choice = float(input("What action would you like to perform? "))

    if choice == "1":
        view()
    elif choice == "2":
        add()
    elif choice == "3":
        remove()
    elif choice == "4":
        search()
    elif choice == "5":
    #    end()
        pass
    else:
        pass

# These are the functions for the actions for the Personal Library
def view():
    books = ["The Hobbit by J.R.R Tolkein", "A Wrinkle in Time by Madeleing L'Engle"]

    pass

def add():
    title = input("What is the Title of the book you want to add: ")
    author = input("Who is the book by: ")
    print(f"You have added {title} by {author}.")
    list = []
    pass

def remove():
    list = []
    #print("book choices" in a list)
    # Display all book items as a numbered list
    bookz = float(input("Enter the number of the item you would like to remove: "))
    print(f"You have removed {bookz} from your Personal Library.")
    print(f"This is your new list of books {books}.")
    pass

def search():
    print("1. Title")
    print("2. Author")
    search_by = float(input("What would you like to search by? "))

    if search_by == "1":
        auhtors_name = input("What is the authors name: ").isalpha()
        print(f"")
    elif search_by == "2":
        title_of_book = input("What is the title of the book: ")
    else:
        print("Please enter a valid number. ")

main()