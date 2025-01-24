#Your code goes between the lines of =======
#===================================================================================

def median(data:list[float]):
    """A function that takes a non-empty list and returns the median of the data in the list.

    Parameters:
        data: a non-empty list with one or more float numbers.

    Returns:
        The median of the data in the list.
    """
    
    if len(data) % 2 == 0:
        
        newData = []
        
        for i in range(len(data)):
            newData.insert(i, data[i])
        
        newData.sort()
        
        return (newData[(len(data)//2)-1] + newData[(len(data)//2)])/2
    
    else:
        newData = []
        
        for i in range(len(data)):
            newData.insert(i, data[i])
        
        newData.sort()
        
        return newData[len(data)//2]


# print(median([3.0,1.0,2.0]))
# print(median([3.0,1.0,2.0,1.0]))


def reverseSort(data:list[int]):
    """A function that takes a list and sorts via mutation descendingly.

    Parameters:
        data: a list with one or more integers.
    
    Returns:
        None
    """
    
    data.sort()
    
    newData = []
        
    for i in range(len(data)):
        newData.insert(i, data[i])
    
    for i in range(len(data)):
        data[i] = newData[-i-1]

data = [1,2,5,-100,3]   
reverseSort(data) 
print(data)

check_median = True
check_reverseSort = True

#===================================================================================
# you should only edit this file above this line
# do not touch below this line

if check_median:
    tests = [
        ([12.3], 12.3),
        ([10.0, 0.0], 5.0),
        ([1.0,3.0,2.0], 2.0),
        ([10.0, 0.0, 10.0, 0.0, 10.0, 0.0, 10.0, 0.0], 5.0)
    ]
    for t in tests:
        before = t[0][:]
        assert median(t[0]) == t[1], "Your median implementation says the median of " + str(t[0]) + " is " + str(t[1])
        assert len(before) == len(t[0]), "Your median implementation changes the list length of its argument " + str(t[0])
        for i in range(len(before)):
            assert before[i] == t[0][i], "Your median implementation mutates the input list"
    print("\nYour median implementation passes all tests. Great!")

import random

if check_reverseSort:
    for i in range(100):
        acc = [] 
        for j in range(100):
            acc.append(random.randint(0,100))
        copy = acc[:]
        reverseSort(acc)
        copy.sort(reverse=True)
        for j in range(100):
            assert copy[j] == acc[j], "Your reverseSort implementation does not yet match .sort(reverse=True). Try your own testing to see why!"
    print("\nYour reverseSort implementation passes all tests. Great!")

print()