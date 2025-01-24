#Your code goes between the lines of =======
#===================================================================================

import random

def pmf(outcomes:dict[str,float]) -> str:
    '''
        INPUT:
            outcomes -- a dictionary mapping strings 
            to the probability with which they will be chosen

        PRECONDITION:
            the values of outcomes are nonnegative and sum to 1

        OUTPUT:
            a key k from outcomes randomly 
            chosen with probability outcomes[k]
    '''

    ks = list(outcomes.keys())
    choice = random.random()
    prob = 0

    for k in ks:
        prob += outcomes[k]
        if prob >= choice:
            return k

    # will always return in the above for-loop
    # because precondition ensures sum of 
    # values will reach 1


def dictUnion(d1:dict, d2:dict) -> dict:
    '''
        INPUT:
            d1, d2 -- dictionaries to union

        OUTPUT:
            a dictionary with all entries across 
            both dictionaries (or just from d1 for 
            keys shared by both d1 and d2)
    ''' 
   
    union = {}

    ks1 = list(d1.keys())
    ks2 = list(d2.keys())

    for k in ks2:
        #if k not in ks1:
        union[k] = d2[k]

    for k in ks1:
        union[k] = d1[k]

    return union


def triangleGrid(n:int) -> list[list[int]]:
    '''
        INPUT:
            n -- the grid height and width

        PRECONDITION:
            n >= 0

        OUTPUT:
            a 2D grid with the diagonal and lower 
            triangle all 1s and the rest all 0s
    '''
    grid = [] 

    for i in range(n):

        grid.append([])

        for j in range(n):

            if j <= i:
                grid[i].append(1)
            else:
                grid[i].append(0)

    return grid

print(triangleGrid(4))


check_pmf = True
check_dictUnion = True
check_triangleGrid = True

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