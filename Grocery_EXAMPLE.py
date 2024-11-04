#Richard Stratigos
#11/04/2024
#Example
#Grade/score example

#Get items from user

userNum = int(input("How many items do you want to purchase"))

# This part different than HW

inStore = ["bread", "milk", "eggs", "beef", "pasta", "ham", "cheese", "grapes", "apples", "tomato"]

#Empty list to hold valid items (hw will be letter grades)

validItems = []

# For loop to allow user to enter items

for items in range(0, userNum):
    #In HW, ask for a float for the grade
    userInput = input(f"Enter grocery item #{items+1}: ")


#In HW, make sure userInput is between 0 and 100
#While grade is invalid,
    #tell them the grade is bad
    # make them try again
    #loop breaks when the grade is valid
#In this program, userInput should be in the list
    while userInput not in inStore:
        print(f"{userInput} is not available")
        userInput = input(f"Enter grocery item #{items+1}: ")

# In this program and in the HW, add valid inputs to a list
#

#append is a function that works at the end of a list

    validItems.append(userInput)
    
#Display something similar to the example, you won't do the below shit
    
#For loop breaks, no more shopping (done adding grades)
print()
print("DONE SHOPPING!!")
print()
print()
print("Here are the items you purchased!")
print("--------" *10)

#valid_items is the thing that changes every time the program runs

for valid_items in validItems:
    print(valid_items)
