# AR Final Extra credit Practice


# Declare and set up lists with different data types and initial Values


my_list = ["Joe", 4, "minutes", 7]
# Add data to and read data from lists using indexing
my_list.insert(1,"Hi")
my_list.append(5)
print(my_list)


# Write loops to go through every item(for loops, list copmrehensions)


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




#for item in empty_list:
    #print(f"These are the items that are in my list {empty_list}")


# Compare two strings using == or comparisons


# find the length of a string
print(len("This is my class"))


# Copy part of a string using slicing
print("Welcome to the end of the world!"[1:12])


# Copy part of a string using + or .join() methods    


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

