# MR 1st Class relationship Notes

# Inheritance "is a"
# Parent Class
class Vehical:
    def __init__(self, model, brand):
        self.brand = brand
        self.model = model

    def move(self):
        print("Move!")

# Child Class
class Car(vehicle):
    pass

class Boat(Vehicle):
    def moce(self):
        print("Sail")

class Plane(Vehicle):
    def move(self):
        print("Fly!")

car = Car("Ford", "Mustang")
boat = Boat("Ibiza", "Touring 20")
plane = Plane("Boeing", "747")

car.move()
boat.move()
plane.move()


# Aggregation
class Library:
    def __init__(self, name, catalog):
        pass

    def add_book(self, book):
        self.catalog.append(book)

    def remove_book(self, book):
        if book in self.catalog:
            self.catalog.pop(book)
        else:
            print("That book isn't im the library.")

    def view_catalog(self):
        for book in self.catalog:
            print(book)

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


    def __str__(self):
        return f"{self.title} by {self.author}"


lib = Library("Provo Library")

lib.add_book(Book("Way of Kingsd", "Brandon Sanderson"))
lib.add_book(Book("fellowship of the Ring", "J.R.R. Tolkein"))
lib.add_book(Book("The Last battle", "C.S. lewis"))