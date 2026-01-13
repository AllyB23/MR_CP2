# MR 1st Financial calculator

#MAIN FUNCTION
def main():
    while True:
        print("Welcome to the MR 1st Financial Calculator.")
        print("Enter the number to select an option")
        print("1. Savings Time Calculator")
        print("2. Compound Interest Calculator")
        print("3. Budget Allocator")
        print("4. Sale Price Calculator")
        print("5. Tip Calculator")
        print("6. Exit")

        choice = input("Choice: ")

        if choice == "1":
            saving()
        elif choice == "2":
            compound_interest()
        elif choice == "3":
            budget_allocator()
        elif choice == "4":
            sale_price()
        elif choice == "5":
            calculate_tip()
        elif choice == "6":
            print("Thank you, Bye.")
            break
        else:
            print("Invalid choice.")


def saving():
    goal = float(input("What amount are you saving to: "))
    print("How often are you contributing?")
    print("1. Weekly")
    print("2. Monthly")
    frequency = input("Choice: ")
    contribution = float(input("How much are you contributing each time: "))
#INNER FUNCTION
    def calculate_time():
        if frequency == "1":
            weeks = goal / contribution
            return f"It will take {int(weeks)} weeks to save ${goal:.2f}"
        else:
            months = goal / contribution
            return f"It will take {int(months)} months to save ${goal:.2f}"

    print(calculate_time())

#FUNCTIONS
def compound_interest():
    starting_amount = float(input("Starting Amount: "))
    rate = float(input("Interest Rate Percent: ")) / 100
    years = int(input("Years Spent Compounding: "))

    total = starting_amount * (1 + rate) ** years
    print(f"At the end of {years} years you will have ${total:.2f}")


def budget_allocator():
    categories = int(input("How many budget categories do you have: "))

    names = [
        "Rent/Mortgage",
        "Transportation",
        "Groceries",
        "Utilities",
        "Savings"
    ]

    income = float(input("What is your monthly income: "))
    percents = []

    for i in range(categories):
        percent = float(input(f"What percent is your {names[i]}: "))
        percents.append(percent)

    for i in range(categories):
        amount = income * (percents[i] / 100)
        print(f"{names[i]} is ${amount:.0f}")


def sale_price():
    cost = float(input("How much does the item originally cost: "))
    discount = float(input("What percent is the discount: "))
    final_price = cost - (cost * discount / 100)
    print(f"The item now costs ${final_price:.2f}")


def calculate_tip():
    bill = float(input("How much is the bill: "))
    percent = float(input("What percent of a tip are you giving: "))
    tip = bill * (percent / 100)
    total = bill + tip
    print(f"The tip amount is ${tip:.2f} and your total is ${total:.2f}")


main()
