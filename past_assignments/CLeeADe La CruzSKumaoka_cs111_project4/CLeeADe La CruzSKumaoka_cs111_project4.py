"""
Purpose: Solution for project 4 (Modeling A Turbulent Particle)
Author: Chanhui Lee, Ava De La Cruz, Soichiro Kumaoka
Date: October 17th, 2024
CS 111, Fall 2024
"""

import turtle
import random
import math
import matplotlib.pyplot as plt

def angle(x, y):
    """Finds the current angle of the particle with respect to the origin.

    Parameters:
        x: x coordinate of the particle
        y: y coordinate of the particle

    Return value:
        angle: the current angle of the particle with respect to the origin.
    """
    if x == 0: # avoid dividing by zero
        x = 0.001
    angle = math.degrees(math.atan(y / x))
    if angle < 0:
        if y < 0:
            angle = angle + 360 # quadrant IV
        else:
            angle = angle + 180 # quadrant II
    elif y < 0:
        angle = angle + 180     # quadrant III
    return angle


def setupWalls(tortoise, openingDegrees, scale, radius):
    """Draws the circle that works as the boundary.

    Parameters:
        tortoise: a Turtle object for drawing the circle and simulating the particle.
        openingDegrees:  the size of the hole in the enclosing circle in degrees.
        scale: a scaling parameter to adjust the size of the drawing.
        radius: the radius of the circle to simulate the movement of the particle in a random walk.
    
    Return value:
        None
    """
    screen = tortoise.getscreen()
    screen.mode('logo')             # east is 0 degrees
    screen.tracer(5)                # speed up drawing
    
    tortoise.up()                   # draw boundary with
    tortoise.width(0.015 * scale)   # shaded background
    tortoise.goto(radius * scale, 0)
    tortoise.down()
    tortoise.pencolor('lightyellow')
    tortoise.fillcolor('lightyellow')
    tortoise.begin_fill()
    tortoise.circle(radius * scale)
    tortoise.end_fill()
    tortoise.pencolor('black')
    tortoise.circle(radius * scale, 360 - openingDegrees)
    tortoise.up()
    tortoise.home()
    
    tortoise.pencolor('blue')       # particle is a blue circle
    tortoise.fillcolor('blue')
    tortoise.shape('circle')
    tortoise.shapesize(0.75, 0.75)
    
    tortoise.width(1)               # set up for walk
    tortoise.pencolor('green')
    tortoise.speed(0)
    tortoise.down()                 # comment this out to hide trail


def escape(openingDegrees, tortoise, draw):
    """Simulates random movements of particle then returns the number of steps taken.

    Parameters:
        openingDegrees: the size of the hole in the enclosing circle in degrees.
        tortoise: a Turtle object for drawing the circle and simulating the particle.
        draw:  a bool indicating whether the simulation should be drawn to the screen.

    Return value:
        steps: the number of steps taken.
    """
    x = y = 0                       # initialize (x, y) = (0, 0)
    radius = 1                      # moving in unit radius circle
    stepLength = math.pi / 128      # std dev of each step
    
    if draw:
        scale = 300                 # scale up drawing
        setupWalls(tortoise, openingDegrees, scale, radius)
    
    steps = 0                       # count of steps taken
    escaped = False                 # has particle escaped yet?
    
    while not escaped:
    
        # one step of a random walk here
        # if the particle reaches the wall:
        #     if it is in the opening, then exit;
        #     otherwise, "bounce" back to previous saved position
        
        prevX, prevY = x, y # save previous position

        # Random walk step
        x = x + random.gauss(0, stepLength)
        y = y + random.gauss(0, stepLength)
        
        
        dist = math.sqrt(x**2 + y**2) # check if the particle hits the boundary
        
        if dist >= radius:
            currentAngle = angle(x, y)
            
            # check if the particle escaped
            if currentAngle >= (360 - openingDegrees) or currentAngle <= 0:
                escaped = True
            else:  
                x, y = prevX, prevY # bounce back to previous position
        
        steps += 1

        if draw:
            tortoise.goto(x * scale, y * scale)  # move particle

    if draw:
        screen = tortoise.getscreen()   # update screen to compensate
        screen.update()                 # for high tracer value

    return steps



def escapeMonteCarlo(openingDegrees, trials):
    """Calculates an approximation of the number of steps that could be expected to be taken by escape function.

    Parameters:
        openingDegrees: the size of the hole in the enclosing circle in degrees.
        trials: the number of trials to simulate escape function.

    Return value:
        totalSteps/trials: the average number of steps required, over the given number of trials, to escape with an opening of openingDegrees degrees.
    """
    totalSteps = 0
    tortoise = turtle.Turtle()
    
    for trial in range(trials):       
        totalSteps += escape(openingDegrees, tortoise, False)
    return totalSteps/trials



def plotEscapeSteps(minOpening, maxOpening, openingStep, trials):
    """Plots both simulation data and exact expectations given by a formula.

    Parameters:
        minOpening: the smallest size of opening to plot data from, in degrees.
        maxOpening: the largest size of opening to plot data from, in degrees.
        openingStep: the increment of opening sizes to plot data from, in degrees.
        trials: the number of trials to simulate escape function.
        
    Return value:
        None
    """
    openingValues = range(minOpening, maxOpening + 1, openingStep)
    empiricalSteps = []
    theoreticalSteps = []

    for opening in openingValues:
        avgSteps = escapeMonteCarlo(opening, trials) * (math.pi / 128) ** 2
        empiricalSteps.append(avgSteps)
        alpha = math.radians(opening)
        tAlpha = 1 / 2 - 2 * math.log(math.sin(alpha / 4))
        theoreticalSteps.append(tAlpha)

    plt.plot(openingValues, empiricalSteps, label="Empirical")
    plt.plot(openingValues, theoreticalSteps, label="Theoretical")
    plt.xlabel('Opening Degrees')
    plt.ylabel('Average Steps')
    plt.title('Modeling A Turbulent Particle')
    plt.legend()
    plt.show()
    


# plotEscapeSteps(10, 180, 10, 1)
# plotEscapeSteps(10, 180, 10, 10)    
# plotEscapeSteps(10, 180, 10, 1000)
