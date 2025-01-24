import random, math


def approxArea(n:int) -> float:
    '''
        INPUT: 
            n -- the number of trials to approximate the area under a sine curve

        OUTPUT: 
            a Monte Carlo approximation of the area under 1 hump of a sine curve
    '''

    hits = 0

    for i in range(n):

        xCoord = random.random() * 4
        yCoord = random.random() 

        if yCoord <= math.sin(xCoord):
            hits += 1

    hitProb = hits / n  # should be close to sine area/rectangle area which is ? / 4

    return 4 * hitProb

print(approxArea(1000000))


