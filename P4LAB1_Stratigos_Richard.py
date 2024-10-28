#Richard Stratigos
#10/28/2024
#P4LAB1
#While_loop to make a square using a turtle


#Import turtle library to use in code
import turtle

#Set up te window and turtle object

window = turtle.Screen()
timmy = turtle.Turtle()

timmy.pensize(6)
timmy.pencolor("green")
timmy.shape("arrow")

#Use a while_loop to draw 4 sides of a square

line = 0
while line<4:
    timmy.right(90)
    timmy.forward(150)
    line +=1

#Use for_loop to draw 3 sides of a triangle

for line1 in range(3):
    timmy.left(120)
    timmy.forward(150)
    
