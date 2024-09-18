# Richard Stratigos
# 09/16/2024
# P1HW1
# Assignment tests student's knowledge of how to write code that collects information from user, processes information collected and display results to user.

print("----Calculating Exponents----")
print()
print()
base_value = int(input("Enter an integer as the base value: "))
exponent_value = int(input("Enter an integer as the exponent: "))
print()
print()
# Convert base_value to integer

base_value = int(base_value)
exponent_value = int(exponent_value)

print(base_value , "raised to the power of" , exponent_value, "is" , base_value**exponent_value, "!!")
print()
print()

print("----Addition and Subtraction----")


# Convert string inputs into integers

start_num = int(input("Enter a starting integer:"))
print()
add_num = int(input("Enter an integer to add:"))
print()
sub_num = int(input("Enter an integer to subtract:"))
print()
print()

# Calculate results

solution = start_num + add_num - sub_num

# Display all varaibles and results

print(start_num, "+", add_num, "-", sub_num, "is equal to", solution)




