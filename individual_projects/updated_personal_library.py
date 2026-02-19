
# MR 1st Updated Personal Library
import csv
import os

# Make a functions to read the CSv File and read as a tuple or as a library
# LOAD LIBRARY FUNCTION 
def load_library(filename):
    library = []
    # Loads the library from a CSV file into a list of dictionaries
        # library = []
        # if not us.path.exists(filename):
        # return library

# Make sure to check for errors'
# iF it is not reading a CsV or if something went wrong


# Another function for saving the library
# SAVE LIBRARY FUNCTION
    # In a variable save the headers of the data stored in the CSV, they should be able to search using these headers
    # with try open the file and save it

# GET INPUT FUNCTION
    # While True loop
        # 

#DISPLAY LIBRARY FUNCTION
    # Displays the library in a simple mode
    # If there is nothing in the library return the print statement that tells the user that it is empty
    # 



# MAIN FUNCTION
def main():
    filename = "personal_library.csv"
    library = load_library(filename)
    unsaved_changes = False
    
# make a main function, orint all of the options that the user has
    # Put this in a while tru loop so it can break if they choose to exit
    while True:
        # Options
        print("1. Show simple list")
        # SHow simple list
        print("2. Show detailed list")
        # show detailed list
        print("3. Add Item")
        # add item
        print("4. Update Item")
        #update iten 
        #delete item
        #save library
        #reload library from file
        #exit(prompt to save if there are any changes)
# MR 2nd Personal Library
import csv

from io import StringIO
data = "title, creator, year, genre"
r = csv.reader(StringIO(data))
for row in r:
    print(row)
# Import a csv DictReader	Read CSV data into dictionaries, using the first row as fieldnames.

# Functions for all of the actions, we will use nested loops and functionds

# Function for Showing the list of the book
# The simple list
# the detailed list

#Funbction for storing the dictionaries of the items on how they can look up and store the item in thwir personal library
# Function for adding an item
# within this function
    #function for deleting an item
# function for updating and item within the adding function

# main function that lets you choose what to do and introduces you to your personal library

