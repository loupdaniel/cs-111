#Your code goes between the lines of =======
#===================================================================================
import random

def vampireApocalypse(v, k, vampires, people):
    """
    Calculates how long before a town with a population of people becomes a town with no humans left in it.

    Parameters:
        v: The number of humans each vampire can convert per day.
        k: The number of vampires that the vampire hunters can kill per day.
        vampires: The initial number of vampires.
        people: The initial number of humans.

    Returns:
        The number of days until all humans are changed to vampires.
    """
    days = 0
    newVampires = 0
    
    if people == 0:
        return days
    

    while people > 0:
        # Calculate new vampires created
        if vampires * v < people:
            newVampires = vampires * v
        else:
            # days += 1
            return days
        
        
        # Update vampire and human populations
        if vampires + newVampires - k > 0:
            vampires = vampires + newVampires - k
        else:
            print("all vampires are eliminated")


        people -= newVampires
        days += 1
    
    return days

print(vampireApocalypse(1,1,1,10))
# print(vampireApocalypse(3,2,4,100))

def loaded():
    """
    Simulates rolling a loaded die with different probabilities.

    Returns:
        The result of the die roll.
    """
    rand = random.random()
    if rand < 0.25:
        roll = 1
    elif rand < 0.375:
        roll = 2
    elif rand < 0.5:
        roll = 3
    elif rand < 0.625:
        roll = 4
    elif rand < 0.75:
        roll = 5
    else:
        roll = 6
    return roll

check_vampireApocalypse = False
check_loaded = False

#===================================================================================
# you should only edit this file above this line
# do not touch below this line

if check_vampireApocalypse:
    assert vampireApocalypse(2,3,4,0) != None, "Your function is not returning anything!"
    assert vampireApocalypse(2,3,4,0) == 0, "It should take 0 days for a town with 0 people to have 0 people left."
    assert vampireApocalypse(1,0,1,10) == 4, "It should take 4 days to turn 10 people into vampires converting 1 per day with no vampire deaths."
    assert vampireApocalypse(1,1,2,10) == 10, "If one person is converted to a vampire per day (because conversion and killing balance out), it should take 10 days to convert 10 people."
    assert vampireApocalypse(3,2,4,100) == 4, "Arguments 3,2,4,100 should return 4 days!"
    print("\nYour vampireApocalypse implementation passes all tests. Great!")

if check_loaded:
    counts = [0] * 6
    rounds = 10 ** 6
    for i in range(rounds):
        roll = loaded()
        assert roll != None, "Your function does not return anything!"
        assert roll == int(roll), "Your function does not return an integer!"
        assert 1 <= roll <= 6, "Your function returns numbers out of range!"
        counts[roll-1] += 1
    for i in [1,6]:
        if counts[i-1] < rounds * 0.24:
            print("\nYour function almost certainly does not roll " + str(i) + " enough")
        if counts[i-1] > rounds * 0.26:
            print("\nYour function almost certainly rolls " + str(i) + " too much")
    for i in [2,3,4,5]:
        if counts[i-1] < rounds * 0.12:
            print("\nYour function almost certainly does not roll " + str(i) + " enough")
        if counts[i-1] > rounds * 0.13:
            print("\nYour function almost certainly rolls " + str(i) + " too much")

    print("\nYour roll function passes all hard tests. "
          +"If nothing else has been printed about this function, great! If something else"
          +" has been printed about this, you may have your probabilities wrong."
          +" But it is probabilistic so testing cannot be sure!")

print()