"""
Purpose: Solution for project 3 (Model predator/prey population dynamics and graph the data)
Author: Chanhui Lee, Ava De La Cruz, Soichiro Kumaoka
Date: October 4th, 2024
CS 111, Fall 2024
"""
import matplotlib.pyplot as plt


def lotkaVolterra(
        prey, preyBirth, preyDeath,
        pred, predBirth, predDeath,
        timeSteps
    ):
    """Simulates the Lotka-Volterra model over a specified number of time steps.

    Parameters:
        prey: the population density of the prey over some area of interest.
        preyBirth: the birth rate of the prey.
        preyDeath: the contribution to the death rate of the prey made by each predator.
        pred: the population density of the predators over the same area of interest.
        predBirth: the contribution to the birth rate of the predators made by each prey.
        predDeath: the death rate of the predators.
        timeSteps: number of time steps to simulate.

    Return value:
        preyPops: a list of floats representing prey population density data.
        predPops: a list of floats representing predator population density data.
    """
    preyPops = [prey]
    
    predPops = [pred]
    
    for t in range(timeSteps):
        newPrey = prey + preyBirth * prey - preyDeath * prey * pred # Calculate new prey population
        newPred = pred - predDeath * pred + predBirth * prey * pred # Calculate new predator population

        # Append the new populations to the lists
        preyPops.append(newPrey)
        predPops.append(newPred)

        # Update the current populations for the next iteration
        prey = newPrey
        pred = newPred

    return preyPops, predPops
    
    
def popWithCC(
        prey, preyBirth, preyDeath, preyCC,
        pred, predBirth, predDeath,
        timeSteps
    ):
    """Simulates the Lotka-Volterra model with prey carrying capacity over a specified number of time steps.

    Parameters:
        prey: the population density of the prey over some area of interest.
        preyBirth: the birth rate of the prey.
        preyDeath: the contribution to the death rate of the prey made by each predator.
        preyCC: the carrying capacity of the prey population.
        pred: the population density of the predators over the same area of interest.
        predBirth: the contribution to the birth rate of the predators made by each prey.
        predDeath: the death rate of the predators.
        timeSteps: number of time steps to simulate.

    Return value:
        preyPops: a list of floats representing prey population density data.
        predPops: a list of floats representing predator population density data.
    """
    preyPops = [prey]

    predPops = [pred]

    for t in range(timeSteps):
        
        newPrey = prey + preyBirth * prey * (1 - prey / preyCC) - preyDeath * prey * pred # Calculate new prey population with carrying capacity
        
        newPred = pred - predDeath * pred + predBirth * prey * pred # Calculate new predator population

        # Append the new populations to the lists
        preyPops.append(newPrey)
        predPops.append(newPred)

        # Update populations for the next iteration
        prey = newPrey
        pred = newPred

    return preyPops, predPops



def plotPops(preyPops, predPops):
    """Plots the prey and predator population densities over time.

    Parameters:
        preyPops: a list of floats representing prey population density data.
        predPops: a list of floats representing predator population density data.
        
    Return value:
        None
    """
    timeSteps = range(len(preyPops))

    plt.plot(timeSteps, preyPops, label='prey') # Plot prey population data
    plt.plot(timeSteps, predPops, label='predator') # Plot predator population data


    plt.xlabel('time')
    plt.ylabel('population density')

    plt.legend()

    plt.show()


"""
# Q1
preyPops, predPops = lotkaVolterra(5, 0.02, 0.015, 5, 0.004, 0.025, 3000)
plotPops(preyPops, predPops)

preyPops, predPops = lotkaVolterra(5, 0.0002, 0.00015, 5, 0.00004, 0.00025, 300000)
plotPops(preyPops, predPops)


# Q2
preyPops, predPops = lotkaVolterra(5, 0.0002, 0.00015, 5, 0.00004, 0.0005, 300000)
plotPops(preyPops, predPops)


# Q3
preyPops, predPops = popWithCC(5, 0.0002, 0.00015, 50, 5, 0.00004, 0.00025, 300000)
plotPops(preyPops, predPops)

preyPops, predPops = popWithCC(5, 0.0002, 0.00015, 50, 5, 0.00004, 0.0005, 300000)
plotPops(preyPops, predPops)
"""