#Your code goes between the lines of =======
#===================================================================================

def binSearch(lst:list[int], target:int):
    """A binary search function that takes an ascendingly sorted list and returns whether target is in that list.

    Parameters:
        lst: an ascendingly sorted list
        target: an integer

    Returns:
        True or False based on whether target is in the given list.
    """
    
    lst.sort()
    
    low = 0
    high = len(lst) - 1
    
    while low <= high:
        
        mid = (low + high) // 2
        
        if lst[mid] == target:
            return True
        elif lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return False

# print(binSearch([2,4,1,5], 5))


def binFind(lst:list[int], target:int):
    """A binary search function that takes an ascendingly sorted list and returns an index i such that lst[i] is target, or alternatively it returns None if target is not in that list.

    Parameters:
        lst: an ascendingly sorted list
        target: an integer

    Returns:
        An index i such that lst[i] is target or None if target is not in the given list.
    """
    
    lst.sort()
    
    low = 0
    high = len(lst) - 1
    
    while low <= high:
        
        mid = (low + high) // 2
        
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return None

# print(binFind([2,4,1,5], 5))



check_binSearch = True  
check_binFind = True

#===================================================================================
# you should only edit this file above this line
# do not touch below this line

import random 
    

def randList(n):
    out = []
    for i in range(n):
        out.append(random.randint(0,10))
    return out


if check_binSearch:
    for i in range(100):
        lst = randList(5)
        lst.sort()
        target = random.randint(0,10)
        assert (binSearch(lst, target)) == (target in lst), "Your binSearch returned the wrong answer for whether " + str(target) + " is in " + str(lst)

    print("\nYour binSearch implementation passes all tests. Congrats!")
    

if check_binFind:
    for i in range(100):
        lst = randList(5)
        lst.sort()
        target = random.randint(0,10)
        got = binFind(lst, target)
        if got == None:
            assert target not in lst, "Your binSearch returned None for the index of " + str(target) + " in " + str(lst)
        else:
            assert lst[got] == target, "Your binSearch returned " + str(got) + " for the index of " + str(target) + " in " + str(lst)

    print("\nYour binFind implementation passes all tests. Congrats!")
    

print()