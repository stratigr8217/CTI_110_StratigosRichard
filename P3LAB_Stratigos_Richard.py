# Richard Stratigos
# 10/21/2024
# P3LAB
# Calculate most efficient coin combination

# Regular Division

print(100/3)

# Floor Division - returns integer portion of quotient

print(100//3)

# Modulo - returns ONLY the remainder

print(100%3)
print(7%4)

# Get amount of money from user as a float
money = float(input("Enter the amount of money as a float: $"))
money = int(money * 100)

# May need to round this value
#money = round(money * 100)

# Get whole dollars from money amount

dollars = money // 100
print(f"Dollars: {dollars}")

# Remove the dollar amount from money

money = money - (dollars * 100)

# Get whole quarters from money amount

quarters = money // 25
print(f"Quarters: {quarters}")
# Remove the quarters amount from money

money = money - (quarters * 25)

# Get whole dimes from money amount

dimes = money // 10
print(f"Dimes: {dimes}")
# Remove the dimes amount from money

money = money - (dimes * 10)

# Get whole nickels from money amount

nickels = money // 5
print(f"Nickels: {nickels}")

# Remove the nickels amount from money

money = money - (nickels * 5)

# Get whole pennies from money amount

pennies = money // 1
print(f"Pennies: {pennies}")

# Remove the pennies amount from money

money = money - (pennies * 1)
