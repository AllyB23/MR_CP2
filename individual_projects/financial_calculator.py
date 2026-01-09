# MR 1st Financial calculator
# MAIN FUNCTION
function = True

#price = input(float("What is the price of the Item you want to calculate? "))
#budget = input(float(""))
#interest = input(float(""))
#def main():
    #print("What function would you like to perform?\n 1. Budget allocator\n 2. Sale Price Calcultor\n 3. Tip calculator\n 4. Compound Interest Calculator")
    #if function == False:
    
    #pass
# INNER FUNCTION
def calculate_tip():
    try:
        bill = float(input("what is the total you want to calculate? "))    
        total = bill*1.12
        print(f"Your total with a 12% tip is {total}")
    except ValueError:
        print("Please enter a valid Number.")


def sale_price():
    try:
        cost = float(input("How much does the item originally cost? "))
        discount = float(input("What percent is the discount? "))
        print("The item now costs {cost*discount}")
    pass
def budget_allocator():
    try:
        categories = int(input("How many budget categories do you have: "))
        category_1 = rent/mortgage
        category_2 = transportation
        category_3 = groceries
        category_4 = utlilities
        category_5 = savings
        monthly_income = float(input("What is your monthly income: "))



    pass
def compound_interest():
    try:
        starting_amount = float(input("What is your starting amount: "))
        interest_rate = starting_amount*1.05
        years = 10
        print(f"At the end of {years} years you will have ${starting_amount*interest_rate}.")
    except ValueError:
        print("Please enter a valid number.")
    pass


compound_interest()