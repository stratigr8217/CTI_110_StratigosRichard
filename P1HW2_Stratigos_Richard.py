# Richard Stratigos
# 09/23/2024
# P1HW2
# CREATE A PROGRAM THAT CALCULATES BUDGET VS TRAVEL EXPENSES

print("---This program calculates and displays travel expenses---")
print()

# Get information on budget

budget = float(input(f"Enter Budget: "))
print()
location = input("Enter your travel destination: ")
print()
gas = float(input("How much do you think you will spend on gas? "))
print()
hotel = float(input("Approximately, how much will you need for accomodation/hotel? "))
print()
food = float(input("Last, how much do you need for food? "))
print()

# Calculate and display input information

balance = budget-gas-hotel-food

print("------Travel Expenses------")
print("Location: ", location)
print("Initial Budget: ", budget)
print()
print("Fuel: ", gas)
print("Accomodation: ", hotel)
print("Food: ", food)
print()
print("Remaining Balance: ", balance)
