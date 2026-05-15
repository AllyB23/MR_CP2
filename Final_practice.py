# AR Final Extra credit Practice
# Declare and set up lists with different data types and initial Values
my_list = ["Joe", 4, "minutes", 7]
# Add data to and read data from lists using indexing
my_list.insert(1,"Hi")
my_list.append(5)
print(my_list)
# Write loops to go through every item(for loops, list comprehensions)
for list in my_list:
    print(list)
# Create empty lists that can change size
empty_list = []
empty_list.insert(1, "Tomato")
empty_list.append("Hello")
print(empty_list)
empty_list.pop()
print(empty_list)
empty_list.append("Fun")
empty_list.remove("Tomato")
print(empty_list)
# Compare two strings using == or comparisons
string1 = "Chocolate"
string2 = "Vanilla"
if string1 == string2:
    print("They are the same!")
else:
    print(f"{string1} and {string2} are different flavors")
# find the length of a string
print(len("This is my class"))
# Copy part of a string using slicing
print("Welcome to the end of the world!"[1:12])
# Combine strings using + or .join() methods    
introductions = "Hello my name is" + " " + "Ally Rosales"
print(introductions)
introduction = ["Hello my name is", "Ally Rosales"]
sentence = " ".join(introduction)
print(sentence)
# find where a substring appears using .find() or .index()
text = "Hello, welcome to your first day of school!"
print(text.find("day"))
text_second = "This is where all your classes are located, on this map"
try:
    print(text_second.index("located"))
except ValueError:
    print("Substring not found!")
# Insert text using string formatting or .replace() methods
fruits = "Apples, grapes, and Oranges"
sentence = f"My favorite fruits are {fruits}"
print(sentence)
"{} has an appointment with {}".format("Crystal", "Gerald")
complete_sentence = "My friend loves, gaming, sports, and sculpting"
new_sentence = complete_sentence.replace("loves", "dislikes")
print(new_sentence)

# STRAND 2: Working with Files

# Create and write to a file
with open("my_notes.txt", "w") as my_file:
    my_file.write("These are my study notes!\n")
    my_file.write("I love coding so much :)\n")

# Read data from a file
with open("my_notes.txt", "r") as my_file:
    content = my_file.read()
    print(content)

# Append more data to the file
with open("my_notes.txt", "a") as my_file:
    my_file.write("Adding one more note for fun!\n")

# Read line by line
with open("my_notes.txt", "r") as my_file:
    for line in my_file.readlines():
        print(line.strip())

# STRAND 3: Creating Your Own Functions

# Function with no parameters
def say_hello():
    print("Hello! Welcome to Computer Programming 2!")

say_hello()

# Function with parameters
def greet_friend(name, grade):
    print(f"Hey {name}, you are in grade {grade}!")

greet_friend("Sofia", 9)

# Function that returns a value
def add_numbers(num1, num2):
    return num1 + num2

result = add_numbers(5, 10)
print(f"The answer is {result}")

# Function with a default parameter
def favorite_color(color="pink"):
    print(f"My favorite color is {color}!")

favorite_color()
favorite_color("purple")

# Global vs local scope
my_school = "Westview High"

def show_school():
    classroom = "Room 204"
    print(f"I go to {my_school} in {classroom}")

show_school()

# Reusable function to avoid repetitive code
def print_star_border():
    print("*" * 30)

print_star_border()
print("Welcome to my program!")
print_star_border()

# STRAND 4: Object-Oriented Programming

# Using built-in classes
my_set = set()
my_set.add("Math")
my_set.add("English")
my_set.add("Coding")
my_set.add("Coding")
print(my_set)

my_dict = dict()
my_dict["name"] = "Ally"
my_dict["grade"] = 9
print(my_dict.keys())
print(my_dict["name"])

# Creating my own class
class Student:
    def __init__(self, name, grade, favorite_subject):
        self.name = name
        self.grade = grade
        self.favorite_subject = favorite_subject

    def introduce(self):
        print(f"Hi! My name is {self.name}, I am in grade {self.grade}, and I love {self.favorite_subject}!")

    def study(self, topic):
        print(f"{self.name} is studying {topic} right now!")

student1 = Student("Ally", 9, "Computer Programming")
student2 = Student("Sofia", 9, "Art")

student1.introduce()
student2.introduce()
student1.study("Python lists")

print(f"{student1.name}'s favorite subject is {student1.favorite_subject}")

# STRAND 5: Problem-Solving and Debugging

def find_biggest_number(numbers):
    print(f"Starting with list: {numbers}")
    biggest = numbers[0]
    for num in numbers:
        print(f"Checking {num} against current biggest {biggest}")
        if num > biggest:
            biggest = num
    return biggest

my_numbers = [3, 17, 5, 42, 8]
print(f"The biggest number is: {find_biggest_number(my_numbers)}")

print(find_biggest_number([1, 2, 3]))
print(find_biggest_number([100]))
print(find_biggest_number([-5, -1, -10]))

# STRAND 8: Programming Careers

team_roles = {
    "Team Leader": "Manages the project and keeps everyone on track",
    "Analyst": "Figures out what the client needs the software to do",
    "Senior Developer": "Writes complex code and helps other developers",
    "Junior Developer": "Writes code and learns from senior developers",
    "Client": "The person or business who asked for the software"
}

print("Software Development Team Roles")
for role, description in team_roles.items():
    print(f"{role}: {description}")

print("Important traits for programmers: creativity, problem-solving, and teamwork")
