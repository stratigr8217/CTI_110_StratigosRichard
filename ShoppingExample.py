# Richard Stratigos
# 09/23/2024
# In class example
# Simulate shopping and give receipt

print("Welcome to ShopCo!")
print()

# Get info of first item purchased

item1 = input("Enter name of first item: ")
price1 = float(input(f"Enter price of {item1}: "))
quantity1 = int(input(f"Enter the quantity of {item1}: "))

# Get info of second item purchased

item2 = input("Enter name of second item: ")
price2 = float(input(f"Enter price of {item2}: "))
quantity2 = int(input(f"Enter the quantity of {item2}: "))

# Get info of third item purchased

item3 = input("Enter name of third item: ")
price3 = float(input(f"Enter price of {item3}: "))
quantity3 = int(input(f"Enter the quantity of {item3}: "))

# Receipt

print()
print("-----ShopCo Receipt----")
print()
print()
print(f"{item1}    {quantity1}     ${price1*quantity1:.2f}")
print()
print(f"{item2}    {quantity2}     ${price2*quantity1:.2f}")
print()
print(f"{item3}    {quantity3}     ${price3*quantity3:.2f}")
print()

# Calculate Subtotal

subtotal = (price1*quantity1) + (price2*quantity2) + (price3*quantity3)

print(f"Subtotal: ${subtotal: .2f}")

tax_amount = 0.07*subtotal
print(f"Tax: {tax_amount: .2f}")

# Calculate final total

print(f"Total: ${subtotal + tax_amount: 2f}")
