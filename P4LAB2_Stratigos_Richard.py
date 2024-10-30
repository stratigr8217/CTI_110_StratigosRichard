#Richard Stratigos
#10/30/2024
#P4LAB2
#Use a for loop and while loop to display positive multiplication tables


#Create a variable to make program run the first time

run_again = "yes"

#While loop to control the entire program

while run_again == "yes":
    
    #Have user enter integer

    userNum = int(input("Enter an integer: "))
    
    #check if userNum is positive
    if userNum >=0:
        #loop to print multiplication
        for num in range(1,13):
            print(f"{userNum} * {num} = {userNum*num}")
        print()
        
#If userNum is negative, tell the user
        
    else:
        print("Program does not handle negative numbers!")

    print()    
    run_again = input("Would you like to run the program again? (yes/no)").lower()

#Loop breaks

print("Exiting program...")




