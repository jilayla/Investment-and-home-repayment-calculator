# This is a simple program that allows the user to access two different financial calculators:
# an investment calculator and a home loan repayment calculator

import math

# Provide information about investment and bond calculation types

print('''
investment  - to calculate the amount of interest you'll earn on your investment
bond        - to calculate the amount you'll have to pay on a home loan''')

# Ask the user if they want to calculate an investment or bond type

user_input = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

# Calculate the total amount at the end of the investment period depending on the interest type

if user_input == "investment":
    investment_deposit = float(input("Please enter the amount of money you are depositing: "))
    investment_interest_rate = float(input("Please enter the interest rate as a percentage: ")) / 100
    investment_duration = float(input("Please enter the number of years you plan on investing: "))
    interest = input("Is the interest 'simple' or 'compound'? ").lower()
    
    if interest == "simple":
        total_amount = investment_deposit * (1 + investment_interest_rate * investment_duration)
        print(f"At the end of the investment period, you will have: {total_amount:.2f}.")
    elif interest == "compound":
        total_amount = investment_deposit * math.pow((1 + investment_interest_rate), investment_duration)
        print(f"At the end of the investment period, you will have: {total_amount:.2f}.")
    else: 
        print("Invalid interest type.")

# Calculate the monthly payments on a home loan

elif user_input == "bond":
    house_value = float(input("Please enter the value of the house: "))
    bond_interest_rate = float(input("Please enter the interest rate as a percentage: ")) / 100
    bond_duration = int(input("Please enter the number of months you plan to take to repay the bond: "))
    repayment = ((bond_interest_rate / 12) * house_value) / (1 - (1 + (bond_interest_rate / 12)) ** -bond_duration)
    print(f"Each month, you'll have to pay: {repayment:.2f}.")

# Error message if no valid input is entered
else:
    print("Invalid input.")
