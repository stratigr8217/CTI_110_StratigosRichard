# Richard Stratigos
# 11/17/2024
# P5LAB
# Self-checkout machine

import random

# Function to calculate and display change breakdown

def disperse_change(change):
    # Define coin values
    dollar = 1.00
    quarter = 0.25
    dime = 0.10
    nickel = 0.05
    penny = 0.01

# Calculate number of each coin
    
    num_dollars = int(change // dollar)
    change %= dollar

    num_quarters = int(change // quarter)
    change %= quarter

    num_dimes = int(change // dime)
    change %= dime

    num_nickels = int(change // nickel)
    change %= nickel

    num_pennies = round(change / penny)  # Round to handle floating-point imprecision

# Display the results
    
    print("\nChange breakdown:")
    print(f"Dollars: {num_dollars}")
    print(f"Quarters: {num_quarters}")
    print(f"Dimes: {num_dimes}")
    print(f"Nickels: {num_nickels}")
    print(f"Pennies: {num_pennies}")

# Main function

def main():
    
# Generate a random float for the total owed
    
    total_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"The total amount owed is: ${total_owed}")

# Prompt user to enter cash provided
    
    while True:
        try:
            cash_provided = float(input("Enter the amount of cash you will put into the self-checkout: $"))
            if cash_provided < total_owed:
                print("Insufficient funds. Please enter an amount greater than or equal to the total owed.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

# Calculate the change owed

    change_owed = round(cash_provided - total_owed, 2)
    print(f"Change owed: ${change_owed}")

# Call the disperse_change function

    disperse_change(change_owed)

# Call the main function

if __name__ == "__main__":
    main()
