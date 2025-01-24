"""
Purpose: Solution for exercise 4.1.1 and 4.1.2
Author: Chanhui Lee
Date: September 20th, 2024
CS 111, Fall 2024
"""

def pond(years, initialPopulation, harvest, annGrowthRate, restockFishAmount):
    """Simulates a fish population in a fishing pond, and
       prints annual population size.
    
    Parameter:
        years: number of years to simulate
        initialPopulation: initial poplutaion of fishes in pond
        harvest: amount of annualy harvested fishes
        annGrowthRate: annual growth rate of fish population
        restockFishAmount: annual amount of restocked fish
    
    Return value: the final population size
    """
    
    population = initialPopulation
    print( 'Year | Population' )
    print( '-----|-----------' )
    for year in range(years):
        population = annGrowthRate * population - harvest + restockFishAmount
        print( '{0:^4} | {1:>9.2f}'.format(year + 1, population))
    
    return population

def main():
    finalPopulation = pond(15, 12000, 1500, 1.08, 500) # The population grows 8% per year with an annual harvest of 1500 and
                                                       # annually restocked with 500 additional fishes.
    print( 'The final population is ' + str(finalPopulation) + '.' )
main()