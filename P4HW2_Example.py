#In-class example similar to P4HW2

#Enter a product or "exit" to terminate

#Create a varalbe to hold ser input

userInput = input('Enter a product or "exit"').capitalize()

#Create variables to hold num of items and total cost

numItems = 0
totalCost = 0


#Loop to control the main program

while userInput.lower() != "exit":
    numItems += 1
    print()
    print(f"Added {userInput} to cart..")
    cost = float(input(f"Enter the cost for {userInput}: $"))
    totalCost += cost
    print()
    userInput = input('Enter a product or "exit"').capitalize()

#Loop breaks

print(f"Total items purchased: {numItems}")
print(f"Total cost of all items: {totalCost}")


#HW needs to print out the number of employees and how much they were paid
