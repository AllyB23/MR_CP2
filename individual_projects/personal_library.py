# MR 2nd Personal Library
# The dictionary to store the books
books = {"The Hobbit by J.R.R Tolkein",
        "A Wrinkle in Time by Madeleine L'Engle",
        "Steelheart by Brandon Sanderson",
        "The Chroincles of Narnia: The horse and His Boy by C.S. Lewis",
        "The Guve by Lois Lowry",
        "Howl's Moving Castle by Diana Wynne Jones",
        "Artemis Fowl by Brandon Mull",
        "Fablehaven by Brandon Mull",
        "Inkheart by Cornelia Funke"
}# I am using a main function for welcoming the user and saying instructions
def main():  # The main function is acting as a lobby for the Personal Library  
    # This is welcoming the user and explaining what to do and how the Personal Library works
    while True:
        print("Welcome to your Personal Library!")
        print("Your Personal Library is able to store your books and have the ability to View, add, remove, or search your library.")
        print("You may choose any of those options by entering the number that corresponds with the action.")
        print("1. View your personal Library")
        print("2. Add to your Personal Library")
        print("3. Remove from your personal Library")
        print("4. Search your Personal Library")
        print("5. Exit your Personal Library")

        choice = input("What action would you like to perform? ")
        # Calls the functions depending what the user wants to do
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
            break # Breaks the code so it is not and endless loop
        else:
            print("Invalid Choice, please try again.")

# These are the functions for the actions for the Personal Library
def view():
    print("\n Your books:")
    for book in sorted(books):
        print(f" - {book}")
# Adds a book to your library
def add():
    new_book = input("What is the Title of the book you want to add: ")
    author = input("Who is the book by: ")
    full_entry = (f"{new_book} by ({author})")
    books.add(full_entry)
    print(f" ' {new_book}' has been added!")
# Removes a book from your library
def remove():
    book_list = sorted(list(books))
    print("\nWhich book would you like to remove: ")
    for i, book in enumerate(book_list, 1):
        print(f"{i}. {book}")
    # removes the book
    try:
        idx = int(input("Enter the number to remove: "))
        if 1 <= idx <= len(book_list):
            removed = book_list[idx-1]
            books.remove(removed)
            print(f"Removed: {removed}")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Please enter a valid number.")# Tells you if the user entered the wrong thing


# Searches for a book in the library
def search():
    print("1. Title")
    print("2. Author")
    search_options = ("Title", "Author")
    choice = input("What would you like to search by? (1 or 2): ")
    
    if choice in ["1", "2"]:
        category = search_options[int(choice)-1]
        query = input(f"What is the {category} name: ").lower()
        
        print(f"\nResults for '{query}':")
        found = False
        for book in books:
            # Check if the search query exists in the book string
            if query in book.lower():
                print(book)
                found = True
        
        if not found:
            print("No matching items found.")
    else:
        print("Invalid search choice.")

# Calls the main function again so they can do anything they want
main()