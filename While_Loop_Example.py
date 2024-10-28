# Richard Statigos
# 10/28/2024
# While-Loop Examples

#Program only runs if user says yes

userChoice = input("Wanna run the program ?").lower()

while userChoice == "yes":
    print("^:^" * 10)
    print("Program is running!")
    print()
    userChoice = input("Run again? ").lower()
    
#Loop break

print("Thanks for using the program, bye!")



# Numeric value to control loop

controller = 0
max_value = int(input("Enter max value: "))

while controller <= max_value:
    #Add one to controller
    print(controller)
    controller += 1
    
#Loop break

print(f"Loop broke because controller hit max value")
print("Controller is", controller)
