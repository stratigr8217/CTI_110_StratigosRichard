# Richard Stratigos
# 10/21/2024
# P3LAB
# Calculate most efficient coin combination

# Get amount of money from user as a float
money = float(input("Enter the amount of money as a float: $"))
money = int(round(money * 100))


if money == 0:
    print("No Change")

# Get whole dollars from money amount

dollars = money // 100
if dollars >= 1:
    if dollars == 1:
        print(f"{dollars} Dollar")
    else: #more than one dollar
        print(f"{dollars} Dollars")
        
# Remove the dollar amount from money

money = money - (dollars * 100)

# Get whole quarters from money amount

quarters = money // 25
if quarters >= 1:
    if quarters == 1:
        print(f"{quarters} Quarter")
    else: #more than one penny
        print(f"{quarters} Quarters")
    
# Remove the quarters amount from money

money = money - (quarters * 25)

# Get whole dimes from money amount

dimes = money // 10
if dimes >= 1:
    if dimes == 1:
        print(f"{dimes} Dime")
    else: #more than one penny
        print(f"{dimes} Dimes")
    
# Remove the dimes amount from money

money = money - (dimes * 10)

# Get whole nickels from money amount

nickels = money // 5
if nickels >= 1:
    if nickels == 1:
        print(f"{nickels} Nickel")
    else: #more than one penny
        print(f"{nickels} Nickels")

# Remove the nickels amount from money

money = money - (nickels * 5)

# Get whole pennies from money amount

pennies = money // 1
if pennies >= 1:
    if pennies == 1:
        print(f"{pennies} Penny")
    else: #more than one penny
        print(f"{pennies} Pennies")

# Remove the pennies amount from money

money = money - (pennies * 1)
