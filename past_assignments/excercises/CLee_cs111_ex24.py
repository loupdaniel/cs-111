#Your code goes between the lines of =======
#===================================================================================

def findMax(lst:list[int]):
    '''
        INPUTS:
            lst -- the given list

        OUTPUT:
            the largest element in the given list
    '''

    maximum = lst[0]

    def searchHelper(i, maximum):
        '''
            INPUT:
                i -- the current index
                maximum -- the current maximum value

            OUTPUT:
                the largest element in the given list
        '''

        if i < len(lst):
            if maximum < lst[i]:
                maximum = lst[i]
            
            return searchHelper(i+1, maximum)
        else:
            return maximum
        
    return searchHelper(0, maximum)

# print(findMax([5,1,457,3]))

def reverse(lst:list[int]):
    '''
        INPUTS:
            lst -- the given list

        OUTPUT:
            a new list in reverse order
    '''
    
    sample = []
    i = -1
    
    def reverseHelper(i, sampleList):
        '''
            INPUT:
                i -- the current negative index
                sampleList -- the list with the reversed elements added

            OUTPUT:
                the reverse of the input list
        '''

        if len(sampleList) == len(lst):
            return sampleList
            
        else:
            sampleList.append(lst[i])
            return reverseHelper(i -1, sampleList)
        
    return reverseHelper(i, sample)

# print(reverse([1,2,3]))

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