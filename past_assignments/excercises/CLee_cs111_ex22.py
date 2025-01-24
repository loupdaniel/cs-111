#Your code goes between the lines of =======
#===================================================================================
import random

def pmf(outcomes:dict[str,float]):
    """    
    INPUTS:
        outcomes --- a dictionary
    
    PRECONDITION:
        assume that the input's values are nonnegative and sum to 1.
    
    OUTPUT:
        one of the keys with probability given by that key's value.
    """
    
    keyList = list(outcomes.keys())
    valList = []
    
    for i in range(len(keyList)):
        valList.append(float(outcomes[keyList[i]]))
    
    valList.sort()
    newKeyList = []
    
    for i in range(len(keyList)):
        for j in range(len(valList)):
            if float(outcomes[keyList[i]]) == valList[j]:
                newKeyList.append(keyList[j])
    
    rand = random.random()
    
    probabilitySum = valList[0]
    index = 0
    
    while probabilitySum <= 1:
        if rand < probabilitySum:
            
            return newKeyList[index]
        else:
            index += 1
            probabilitySum += valList[index]
        
# print(pmf({"heads":0.5, "tails":0.5}))

def dictUnion(d1: dict, d2: dict):
    """A function that returns a dictionary that contains all of the inputs' key-value pairs. If a key is present in both dictionaries, however, it should only be paired with the value belonging to the first dictionary d1. 

    Parameters:
        d1: a dictionary
        d2: a dictionary

    Returns:
        result: a dictionary that contains all of the inputs' key-value pairs.
    """
    
    keyListD1 = list(d1.keys())
    valListD1 = list(d1.values())
    
    keyListD2 = list(d2.keys())
    valListD2 = list(d2.values())
    
    result = {}
    
    newKeyListD2 = []
    newValListD2 = []
    
    for i in range(len(keyListD2)):
        if keyListD2[i] not in keyListD1:
            newKeyListD2.append(keyListD2[i])
            newValListD2.append(valListD2[i])
    
    
    totalKeyList = keyListD1 + newKeyListD2
    totalValList = valListD1 + newValListD2
    
    
    for i in range(len(totalKeyList)):
        result[totalKeyList[i]] = totalValList[i]
    
    return result

#print(dictUnion({1:"a", 2:"b"},{1:"c", 3:"d"}))

def triangleGrid(n:int):
    """A function that returns an n*n grid in which all cells on and below the main diagonal contain a 1 and the rest of the cells contain a 0

    Parameters:
        n: an integer defining the size of the grid

    Returns:
        outerList: an n*n grid in which all cells on and below the main diagonal contain a 1 and the rest of the cells contain a 0
    """
    
    outerList = []
    
    for i in range(n):
        innerList = []
        
        for j in range(n):
            if j < i+1:
                innerList.append(1)
            else:
                innerList.append(0)
        
        outerList.append(innerList)
        
    return outerList

print(triangleGrid(5))


check_pmf = False
check_dictUnion = False
check_triangleGrid = False

#===================================================================================
# you should only edit this file above this line
# do not touch below this line

import random, string

if check_pmf:
    heads = 0
    tails = 0
    for i in range(1000):
        flip = pmf({"heads":0.5, "tails":0.5})
        assert flip in ["heads", "tails"], "Your pmf function is returning " + flip + " even when it should only be able to return heads or tails"
        if flip == "heads":
            heads += 1 
        else:
            tails += 1
    if heads >= 600 or heads <= 400:
        print("Your pmf probabilities are likely wrong, but testing cannot tell for sure!")
    

    a = 0
    b = 0
    c = 0
    for i in range(1000):
        flip = pmf({"a":0.3, "b":0.05, "c":0.65})
        assert flip in ["a", "b", "c"], "Your pmf function is returning " + flip + " even when it should only be able to return a, b, or c"
        if flip == "a":
            a += 1 
        elif flip == "b":
            b += 1
        else:
            c += 1
    if a >= + 400 or a <= 200 or b >= 150 or b <= 20 or c >= 750 or c <= 550:
        print("Your pmf probabilities are likely wrong, but testing cannot tell for sure!")
    
    print("\nYour pmf function passes all tests. Great job!")
    print("Check your work though if any warnings were printed about probability.")


if check_dictUnion:
    for i in range(1000):
        d1 = {} 
        d2 = {} 
        for letter in string.ascii_letters:
            choice = random.randint(1,3)
            if choice <= 2:
                d1[letter] = random.random()
            if choice >= 2:
                d2[letter] = random.random()
        union = dictUnion(d1,d2)
        uks = list(union.keys())
        d1ks = list(d1.keys())
        d2ks = list(d2.keys())
        for k in uks:
            assert k in d1ks or k in d2ks, "Your dictUnion return has the key " + str(k) + " but it should not"
        for k in d1ks:
            assert k in uks, "Your dictUnion return misses key " + str(k) + " from the first dictionary"
            assert d1[k] == union[k], "Your dictUnion gives key " + str(k) + " the value " + str(union[k]) + " but it should have d1's value " + str(d1[k])
        for k in d2ks:
            assert k in uks, "Your dictUnion return misses key " + str(k) + " from the second dictionary"
            if k not in d1ks:
                assert d2[k] == union[k], "Your dictUnion gives key " + str(k) + " the value " + str(union[k]) + " but it should have d2's value " + str(d2[k])
    print("\nYour dictUnion function passed all tests. Great job!")


if check_triangleGrid:
    t1 = triangleGrid(1)
    assert t1 == [[1]], "Your triangleGrid function returns " + str(t1) + " for argument 1 when it should return [[1]]"
    t2 = triangleGrid(2)
    assert t2 == [[1,0],[1,1]], "Your triangleGrid function returns " + str(t1) + " for argument 2 when it should return [[1,0],[1,1]]"
    t0 = triangleGrid(0)
    assert t0 == [], "Your triangleGrid function returns " + str(t1) + " for argument 0 when it should return []"
    t100 = triangleGrid(100)
    for i in range(100):
        for j in range(100):
            if j <= i:
                assert t100[i][j] == 1, "Your triangleGrid function mistakenly doesn't put a 1 in row " + str(i) + " column " + str(j)
            else:
                assert t100[i][j] == 0, "Your triangleGrid function mistakenly doesn't put a 0 in row " + str(i) + " column " + str(j)
    print("\nYour triangleGrid function passed all tests. Great job!")

print()