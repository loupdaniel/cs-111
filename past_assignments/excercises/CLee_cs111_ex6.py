"""
Purpose: Solution for exercise 2.4.4
Author: Chanhui Lee
Date: September 14th, 2024
CS 111, Fall 2024
"""

import turtle
import math # math module (more in the next chapter)

def drawCircle(radius):
    """
    Draws a circle with the given radius using turtle graphics.
    
    Parameters:
        radius: the radius of the circle.
    
    Return value:
        None
    """

    #Create two turtle objects for drawing the upper and lower semicircles
    topTurtle = turtle.Turtle()
    bottomTurtle = turtle.Turtle()
    screen = topTurtle.getscreen()

    #Set the coordinate so that the circle fits in the window
    margin = 10  #Define margin value for creating extra space
    screen.setworldcoordinates(-radius - margin, -radius - margin, radius + margin, radius + margin)

    #Hide turtles
    topTurtle.hideturtle()
    bottomTurtle.hideturtle()
    
    #Lift pen to move without drawing
    topTurtle.penup()
    bottomTurtle.penup()

    #Move both turtles to the starting point (-radius, 0)
    topTurtle.goto(-radius, 0)
    bottomTurtle.goto(-radius, 0)

    #Start drawing with putting the pen down
    topTurtle.pendown()
    bottomTurtle.pendown()

    #Draw the circle by plotting points along the circumference
    for x in range(-radius, radius + 1):
        topTurtle.goto(x, math.sqrt(radius ** 2 - x ** 2)) #Draw upper semicircle, sqrt is square root
        bottomTurtle.goto(x, -math.sqrt(radius ** 2 - x ** 2)) #Draw lower semicircle, sqrt is square root

def main():
    """
    Draws a circle with the radius of 100.
    """
    drawCircle(100)

main()



"""
Purpose: Solution for exercise 2.5.6
Author: Chanhui Lee
Date: September 14th, 2024
CS 111, Fall 2024
"""

import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2+(y1-y2)**2)