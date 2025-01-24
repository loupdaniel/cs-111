#Your code goes between the lines of =======
#===================================================================================
# When you are done the coding and testing, put a comment in the code file that records
# a probability returned by monteMonty. In that comment, try explaining why you see the
# probability that you do. Is it what you expected?
import random

door_0 = 1
door_1 = 2
door_2 = 3

def montyHall(choice, switch):
    """Decides whether win win or lose 

    Parameters:
        choice: original door choice
        switch: whether we decide to switch doors or not

    Returns:
        The result of the Monty Hall problem
    """
    if choice == door_0 and switch == False:
        return False
    elif choice == door_0 and switch == True:
        return True
    elif choice == door_1 and switch == False:
        return True
    elif choice == door_1 and switch == True:
        return False
    elif choice == door_2 and switch == False:
        return False
    elif choice == door_2 and switch == True:
        return True
    
# print(montyHall(2, False))
    
def monteMonty(trials):
    """Finds the probability of winning if we decide to switch doors

    Parameters:
        trials: number of trials

    Returns:
        the probability of winning if we decide to switch doors based on how many trials the function receives
    """
    winCount = 0
    
    for trial in range(trials):
        
        randi = random.random()
        
        if randi < 0.33:
            doorNum = 1
        elif randi < 0.66:
            doorNum = 2
        else:
            doorNum = 3
        
        res = montyHall(doorNum, True)
        
        if res == True:
            winCount += 1

    return winCount/trials

# print(monteMonty(1000))
# print(monteMonty(10000))

# By adding a code line, print(monteMonty(10000)), it shows the result as 0.6776
# The result is close to the probability of 2/3 ≈ 0.6667 for winning the Monty Hall problem when always switching doors. The probability is what I have expected.


def fine(speedLimit, clockedSpeed):
    """Determines the fine amount

    Parameters:
        speedLimit: the speed limit in a nearby town
        clockedSpeed: the actual speed recorded

    Returns:
        The amount of fine calculated
    """
    if speedLimit >= clockedSpeed:
        return 0
    if speedLimit < clockedSpeed:
        if clockedSpeed > 90:
            return 200 + 50 + 5 * (clockedSpeed - speedLimit)
        else:
            return 50 + 5 * (clockedSpeed - speedLimit)

# print(fine(20, 20))
# print(fine(20, 100))

check_montyHall = True
check_monteMonty = True
check_fine = True

#===================================================================================
# you should only edit this file above this line
# do not touch below this line

if check_montyHall:
    assert montyHall(1,True) != None, "Your montyHall does not return anything!"
    assert montyHall(1, True), "Your montyHall fails at door 1 with switching."
    assert not montyHall(1, False), "Your montyHall fails at door 1 without switching."
    assert montyHall(2, False), "Your montyHall fails at door 2 without switching."
    assert not montyHall(2, True), "Your montyHall fails at door 2 with switching."
    assert montyHall(3, True), "Your montyHall fails at door 3 with switching."
    assert not montyHall(3, False), "Your montyHall fails at door 3 without switching."
    print("\nYour montyHall passes all tests. Great!")

if check_monteMonty:
    assert monteMonty(10) != None, "Your monteMonty does not return anything!"
    assert monteMonty(10) <= 1, "Your monteyMonty is returning probabilities greater than 1!"
    assert monteMonty(10) >= 0, "Your monteyMonty is returning probabilities less than 0!"
    if monteMonty(1000000) < 0.25:
        print("Your monteMonty function's probabilities are very likely too low. But this could be wrong!")
    if monteMonty(1000000) > 0.75:
        print("Your monteMonty function's probabilities are very likely too high. But this could be wrong!")
    print("\nYour monteMonty passes the basic tests. Great! Make sure to comment the probability you see!")
    

if check_fine:
    assert fine(100,50) != None, "Your fine function does not return anything!"
    assert fine(100,50) == 0, "Your fine function is fining people under the speed limit!"
    assert fine(30,30) == 0, "Your fine function is fining people going exactly the speed limit!"
    assert fine(0,1) == 55, "Your fine function is not fining people the correct amount for going 1 mph over!"
    assert fine(5,10) == 50 + 5 * 5, "Your fine function is not fining people the correct amount for going 5 mph over!"
    assert fine(25,100) == 5 * 75 + 250, "Your function is not imposing the additional fine for going over 90 mph when speeding!"
    assert fine(200,150) == 0, "Your fine function is fining people under the speed limit (but over 90 mph)!"
    print("\nYour fine implementation passes all the tests. Great!")

print()