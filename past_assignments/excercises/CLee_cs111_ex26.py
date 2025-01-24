#Your code goes between the lines of =======
#===================================================================================

def ins(lst:list[int], x:int):
    """A function that takes an ascendingly sorted list lst and number x and returns an ascendingly sorted list containing all the elements from lst in addition to x. 

    Parameters:
        lst: an ascendingly sorted list
        target: an integer

    Returns:
        An ascendingly sorted list containing all the elements from lst in addition to x.
    """
    
    result = []
    insertStatus = False
    i = 0
    
    while i < len(lst):
        if not insertStatus and x <= lst[i]:
            result.append(x)
            insertStatus = True
            
        result.append(lst[i])
        i += 1
        
    if not insertStatus:
        result.append(x)
        
    return result

# print(ins([1,2,4], 3))


def insertionSort(lst):
    
    acc = []
    
    for elt in lst:
        acc = ins(acc, elt)
        
    return acc




def merge(lst1:list[int], lst2:list[int]):
    """A function that takes two ascendingly sorted lists and returns an ascendingly sorted list containing all the elements of both.

    Parameters:
        lst1: an ascendingly sorted list
        lst2: an ascendingly sorted list

    Returns:
        An ascendingly sorted list containing all the elements of both.
    """
    
    result = []
    
    for i in range(len(lst1)):
        result.append(lst1[i])
    for j in range(len(lst2)):
        result.append(lst2[j])
    
    count = 0
    
    while count < len(result):
        for i in range(len(result)-1):
            if result[i] > result[i+1]:
                save = result[i]
                result[i] = result[i+1]
                result[i+1] = save
        count += 1
    
    
    return result

# print(merge([2,4], [1,3]))


check_ins = True
check_merge = True

#===================================================================================
# you should only edit this file above this line
# do not touch below this line

import random 
    

def randList(n):
    out = []
    for i in range(n):
        out.append(random.randint(0,10))
    return out


if check_ins:
    for i in range(100):
        lst = randList(5)
        lst.sort()
        target = random.randint(0,10)
        result = ins(lst, target)
        assert target in result, "The result of ins(" + str(lst) + ", " + str(target) + ") does not contain " + str(target)
        for elt in lst:
            assert elt in result, "The result of ins(" + str(lst) + ", " + str(target) + ") does not contain " + str(elt)
        assert result == sorted(result), "Your ins returned the unsorted list " + str(result)

    print("\nYour ins implementation passes all tests. Congrats!")
    

if check_merge:
    for i in range(100):
        lst1 = randList(5)
        lst1.sort()
        lst2 = randList(5)
        lst2.sort()
        result = merge(lst1, lst2)
        for elt in lst1 + lst2:
            assert elt in result, "The result of merge(" + str(lst1) + ", " + str(lst2) + ") does not contain " + str(elt)
        assert result == sorted(result), "Your merge returned the unsorted list " + str(result)
        
    print("\nYour merge implementation passes all tests. Congrats!")
    

print()