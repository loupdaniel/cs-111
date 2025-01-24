#Your code goes between the lines of =======
#===================================================================================

def selectMin(lst:list[int]):
    """A function that takes a nonempty list and returns a tuple of the lowest element in the list paired with a list of the rest of the elements in any order.

    Parameters:
        lst: a list containing integers.

    Returns:
        A tuple of the lowest element in the list paired with a list of the rest of the elements in any order.
    """
    
    minNum = lst[0]
    saveIndex = 0
    
    for i in range(1, len(lst)):
        if minNum >= lst[i]:
            minNum = lst[i]
            saveIndex = i
            
    lst.pop(saveIndex)
            
    result = (minNum, lst)
    
    return result

# print(selectMin([3,1,4,1,5,9]))

def selectionSort(lst:list[int]):
    """A function that sorts the given list ascendingly.

    Parameters:
        lst: a list containing integers.

    Returns:
        An ascendingly sorted list.
    """
    
    result = []
    
    
    while len(lst) != 0:
        minNum = selectMin(lst)
        result.append(minNum[0])
    
    return result

# print(selectionSort([3,1,4,1,5,9]))


check_selectMin = True
check_selectionSort = True

#===================================================================================
# you should only edit this file above this line
# do not touch below this line

import random 
    

def randList(n):
    out = []
    for i in range(n):
        out.append(random.randint(0,10))
    return out


if check_selectMin:
    for i in range(100):
        lst = randList(10)
        lstCopy = lst[:]
        mini, rest = selectMin(lst)
        assert mini == min(lstCopy), "Your selectMin returned " + str(mini) + " as the min of " + str(lstCopy)
        assert sorted([mini] + rest) == sorted(lstCopy), "Your selectMin does not return the same elements that were present in the original input"

    print("\nYour selectMin implementation passes all tests. Congrats!")
    

if check_selectionSort:
    for i in range(100):
        lst = randList(6)
        correct = lst[:]
        correct.sort()
        s = selectionSort(lst)
        assert s == correct, "Your selectionSort sorts " + str(lst) + " into " + str(s)
    print("\nYour selectionSort implementation passes all tests. Congrats!")
    

print()