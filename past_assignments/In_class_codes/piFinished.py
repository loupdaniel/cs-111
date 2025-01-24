import random


def distance(x1:float, y1:float, x2:float, y2:float) -> float:
    '''
        INPUTS:
            x1 -- x coordinate of first point
            y1 -- y coordinate of first point 
            x2 -- x coordinate of second point 
            y2 -- y coordinate of second point 

        OUTPUT: 
            distance from first to second point
    '''
    xDif = x1 - x2 
    yDif = y1 - y2 
    return (xDif**2 + yDif**2) ** 0.5


def approxPi(n:int) -> float:
    '''
        INPUT: 
            n -- the number of trials to approximate pi 

        OUTPUT: 
            a Monte Carlo approximation of pi
    '''

    hits = 0

    for i in range(n):

        xCoord = random.random() 
        yCoord = random.random() 

        if distance(0.5, 0.5, xCoord, yCoord) <= 0.5:
            hits += 1

    hitProb = hits / n  # should be close to circle/square area which is (pi/4) / 1

    return 4 * hitProb

print(approxPi(100))


