#Richard Stratigos
#10/08/2024
#P2HW1
#CREATE A PROGRAM THAT CALCULATES BUDGET VS TRAVEL EXPENSES



print("---This program calculates and displays travel expenses---")
print()

# Get information on budget

budget = float(input(f"Enter Budget: $"))
print()
location = input("Enter your travel destination: ")
print()
gas = float(input("How much do you think you will spend on gas? $"))
print()
hotel = float(input("Approximately, how much will you need for accommodation/hotel? $"))
print()
food = float(input("Last, how much do you need for food? $"))
print()

# Calculate and display input information

balance = budget-gas-hotel-food

print("------Travel Expenses------")
print(f"{'Location:':<18}{location:<25}")
print(f"{'Initial Budget: ':<18}${budget:<25,.2f}")
print(f"{'Fuel: ':<18}${gas:<25,.2f}")
print(f"{'Accommodation: ':<18}${hotel:<25,.2f}")
print(f"{'Food: ':<18}${food:<25,.2f}")
print("----------------------------")
print()
print(f"{'Remaining Balance: ':<18}{balance:<25,.2f}")
