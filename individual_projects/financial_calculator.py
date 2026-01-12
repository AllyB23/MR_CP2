# MR 1st Financial calculator
# MAIN FUNCTION
function = True

#price = input(float("What is the price of the Item you want to calculate? "))
#budget = input(float(""))
#interest = input(float(""))
#def main():
    #print("What function would you like to perform?\n 1. Budget allocator\n 2. Sale Price Calcultor\n 3. Tip calculator\n 4. Compound Interest Calculator")
    #if function == False:
def main():

    while True:
        print("Welcome to the MR 1st Financial Calculator.")
        print("What function would you like to perform?")
        print(" 1. Savings Time Calculator")
        print(" 2. Budget allocator")
        print(" 3. Sale Price Calculator")
        print(" 4. Tip calculator")
        print(" 5. Compound Interest Calculator")
        print(" 6. Exit.")

        choice = input("Enter the number of your choice: ")
        if choice == '1':
            saving()
        elif choice == '2':
            budget_allocator()
        elif choice == '3':
            sale_price()
        elif choice == '4':
            calculate_tip()
        elif choice == '5':
            compound_interest()
        elif choice == '6':
            print("Thank you, Bye.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
# INNER FUNCTION
def saving():
    float(input("What amount are you saving to? "))
    float(input("How aften are you contributing? "))
    print(" 1. Weekly\n 2. Monthly")
    float(input("How much are you contributing each time? "))
    print("")
          
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
        discount_amount = cost * (discount / 100)
        final_price = cost - discount_amount
        print(f"The item now costs ${final_price:.2f} (You saved ${discount_amount:.2f}).")
    except ValueError:
        print("Please enter a valid number.")
def budget_allocator():
    try:
        categories = int(input("How many budget categories do you have: "))
        categories_list = ["category_1 = rent/mortgage",
        "category_2 = transportation",
        "category_3 = groceries",
        "category_4 = utlilities",
        "category_5 = savings"]
        monthly_income() = float(input("What is your monthly income: "))
        rent_mortgage_percent() = float(input("What percent i syour Rent/Mortgage?"))
        transportation_percent() = float(input("What perent is your transportation?"))
        groceries_percent() = float(input("What percent is your Utilities? "))
        savings_percent() = float(input("What percent is your savings?" ))
        if categories_list == '1':
            rent_mortgage_percent() 


    except ValueError:
        print("Please enter a valid number.")


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


main()