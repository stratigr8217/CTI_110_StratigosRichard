#Richard Stratigos
#10/04/2024
#P2LAB2
#Create a dictionary that stores key and value pairs

vroom = {"Camaro":18.21, "Prius":52.36, "Model S":110, "Silverado":26}


#Print keys in dictionary

print(vroom.keys())


#Get a vroom key from user

GoFast = input(" Enter a vehicle to see it's mpg: ")


#Display mpg for the GoFast

print(f"The {GoFast} gets {vroom[GoFast]} mpg.")


#Get mileage estimate from user

mileage = int(input(f"How many miles will you drive the {GoFast}? "))


#Calculate gallons of gas needed

gallons = mileage/vroom[GoFast]


#Display gallons of gas needed

print(f"{gallons:.2f} gallon(s) of gas are needed to drive the {GoFast} {mileage} miles.")
