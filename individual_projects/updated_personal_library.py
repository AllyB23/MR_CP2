
# MR 1st Updated Personal Library
import csv
import os
# The list to store the books (each item is a dictionary)
library = []
# The CSV file
FILE_NAME = "library.csv"

FIELDS = ["title", "creator", "year", "genre", "format", "rating", "notes"]

# Function to load the CSV file
def load_library():
    global library

    if not os.path.exists(FILE_NAME):
        # Create file with header if it doesn't exist
        with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDS)
            writer.writeheader()
        library = []
        return

    library = []

    with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                row["year"] = int(row["year"])
                library.append(row)
            except:
                print("⚠ Skipping invalid row in file.")


# Function to save to CSV
def save_library():
    with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writeheader()
        for item in library:
            writer.writerow(item)

    print("Library saved successfully.")


# View simple list
def view_simple():
    print("\n Your Library (Simple View):")
    if not library:
        print("Library is empty.")
        return

    for i, item in enumerate(library, 1):
        print(f"{i}. {item['title']} by {item['creator']}")


# View detailed list
def view_detailed():
    print("\n Your Library (Detailed View):")
    if not library:
        print("Library is empty.")
        return

    for i, item in enumerate(library, 1):
        print(f"\nItem #{i}")
        for field in FIELDS:
            print(f"{field.capitalize()}: {item[field]}")
        print("-" * 30)


# Add a new item
def add():
    print("\nAdd a New Item")

    title = input("Title: ")
    creator = input("Creator (author/artist/director): ")

    # Validate year of the book in the library
    while True:
        year_input = input("Year: ")
        if year_input.isdigit():
            year = int(year_input)
            break
        else:
            print("Invalid year. Please enter a number.")

    genre = input("Genre: ")
    format_type = input("Format (optional): ")
    rating = input("Rating (optional): ")
    notes = input("Notes (optional): ")

    item = {
        "title": title,
        "creator": creator,
        "year": year,
        "genre": genre,
        "format": format_type,
        "rating": rating,
        "notes": notes
    }

    library.append(item)
    print(f"'{title}' has been added!")


# Remove an item
def remove():
    if not library:
        print("Library is empty.")
        return

    view_simple()

    try:
        idx = int(input("Enter the number to remove: "))
        if 1 <= idx <= len(library):
            removed = library.pop(idx - 1)
            print(f"Removed: {removed['title']}")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Please enter a valid number.")


# Update an item in the library
def update():
    if not library:
        print("Library is empty.")
        return

    view_simple()

    try:
        idx = int(input("Enter the number to update: "))
        if 1 <= idx <= len(library):
            item = library[idx - 1]

            print("Leave blank to keep current value.")

            for field in FIELDS:
                new_value = input(f"{field.capitalize()} ({item[field]}): ")

                if new_value:
                    if field == "year":
                        if new_value.isdigit():
                            item[field] = int(new_value)
                        else:
                            print("Invalid year. Keeping old value.")
                    else:
                        item[field] = new_value

            print("Item updated.")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Please enter a valid number.")


# Search function
def search():
    # If statements for the choices to search by
    if not library:
        print("Library is empty.")
        return

    print("1. Title")
    print("2. Creator")
    print("3. Genre")

    choice = input("Search by (1-3): ")

    if choice not in ["1", "2", "3"]:
        print("Invalid search choice.")
        return

    query = input("Enter search term: ").lower()

    print("\nResults:")
    found = False
#   looking for the item in the library
    for item in library:
        if choice == "1" and query in item["title"].lower():
            print(f"{item['title']} by {item['creator']}")
            found = True
        elif choice == "2" and query in item["creator"].lower():
            print(f"{item['title']} by {item['creator']}")
            found = True
        elif choice == "3" and query in item["genre"].lower():
            print(f"{item['title']} by {item['creator']}")
            found = True

    if not found:
        print("No matching items found.")


# Main function (Lobby)
def main():
    load_library()
    unsaved_changes = False
#   While loop so the program can keep running
    while True:
        print("\nWelcome to your Personal Library!")
        print("Here is a list of options that you can choose from to get started!")
        print("1. Show simple list")
        print("2. Show detailed list")
        print("3. Add item")
        print("4. Update item")
        print("5. Remove item")
        print("6. Search")
        print("7. Save library")
        print("8. Reload from file")
        print("9. Exit")

        choice = input("What action would you like to perform? ")

        if choice == "1":
            view_simple()
        elif choice == "2":
            view_detailed()
        elif choice == "3":
            add()
            unsaved_changes = True
        elif choice == "4":
            update()
            unsaved_changes = True
        elif choice == "5":
            remove()
            unsaved_changes = True
        elif choice == "6":
            search()
        elif choice == "7":
            save_library()
            unsaved_changes = False
        elif choice == "8":
            load_library()
            unsaved_changes = False
            print("Library reloaded.")
        elif choice == "9":
            if unsaved_changes:
                save_choice = input("You have unsaved changes. Save before exiting? (y/n): ")
                if save_choice.lower() == "y":
                    save_library()
            print("Thank You, goodbye.")
            break # BReaks the loops so the code can stop running
        else:
            print("Invalid Choice, please try again.")


# Runs the program
if __name__ == "__main__":
    main()
