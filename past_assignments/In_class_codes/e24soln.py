#Your code goes between the lines of =======
#===================================================================================


def findMax(lst:list[int]) -> int:
    '''
        INPUT:
            lst -- the list over which to find the max
        
        OUTPUT:
            the largest element in lst

        PRECONDITION:
            len(lst) >= 1

        SIDE-EFFECT:
            lst will be mutated to be empty
    '''

    if len(lst) == 1:
        return lst[0]
    else:

        fst = lst.pop(0)
        maxOfRest = findMax(lst)

        if fst >= maxOfRest:
            return fst 
        else:
            return maxOfRest
        



def reverse(lst:list[int]) -> list[int]:
    '''
        INPUT:
            lst -- the list to reverse

        OUTPUT:
            lst reversed

        SIDE-EFFECT:
            lst is mutated to be empty
    '''
    
    if lst == []:
        return [] 
    else:
        fst = lst.pop(0)
        rev = reverse(lst)
        rev.append(fst)
        return rev




check_findMax = True  
check_reverse = True

#===================================================================================
# you should only edit this file above this line
# do not touch below this line

import random 

def randList(n):
    out = []
    for i in range(n):
        out.append(random.randint(0,100))
    return out

if check_findMax:
    for i in range(100):
        lst = randList(5)
        got = findMax(lst[:]) 
        correct = max(lst)
        assert got == correct, "Your findMax returned " + str(got) + " for the max of " + str(lst)

    
    print("\nYour findMax implementation passes all tests. Congrats!")
    

if check_reverse:

    def rev(lst):
        out = [] 
        for elt in lst:
            out = [elt] + out
        return out

    for i in range(100):
        lst = randList(5)
        got = reverse(lst[:]) 
        correct = rev(lst)
        assert got == correct, "Your reverse returned " + str(got) + " for the reverse of " + str(lst)
    
    print("\nYour reverse implementation passes all tests. Congrats!")


print()