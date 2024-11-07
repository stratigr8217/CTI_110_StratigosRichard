#Richard Stratigos
#10/04/2024
#P2LAB1
#Defining Circle Formulas

#Import math library

import math

#Get the radius from user

GetR = float(input("What is the radius of the circle?"))

print()

#Calculate diameter of the circle

GetD = 2 * GetR

#Display diameter with 1 decimal place

print(f"The diameter of the circle is {GetD:.1f}")

#Calculate circumference of the circle

GetC = 2 * math.pi * GetR
print()

#Display circumference with 2 decimal places

print(f"The circumference of the circle is {GetC:.2f}")
print ()


#Calculate area of the circle

GetA = math.pi * (GetR ** 2)
GetA2 = math.pi * math.pow (GetR, 2)

#Display area with 3 decimal places

print(f"The area of the circle is {GetA:.3f} \n")
print(f"The area of the circle is {GetA2:.3f} \n")
