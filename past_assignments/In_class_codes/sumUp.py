

def sumUpWhile(lst:list[int]) -> int:
    '''
        INPUT:
            lst -- the list of numbers to sum

        OUTPUT:
            the sum of the numbers in lst
    '''

    total = 0
    i = 0 

    while i < len(lst):
        total += lst[i]
        i += 1

    return total


def sumUpRec(lst:list[int]) -> int:
    '''
        INPUT:
            lst -- the list of numbers to sum

        OUTPUT:
            the sum of the numbers in lst
    '''
     
    def sumHelper(lst:list[int]) -> int:
        '''
            INPUT:
                lst -- the list of numbers to sum

            OUTPUT:
                the sum of the numbers in lst

            SIDE-EFFECT:
                lst is made empty
        '''

        if lst == []:
            return 0
        else:
            return lst.pop(0) + sumHelper(lst)
        
    return sumHelper(lst[:])





import random

for i in range(100):

    lst = [] 
    for j in range(50):
        lst.append(random.randint(0,100))
    
    assert sumUpRec(lst) == sumUpWhile(lst)

print("\nThey match!\n")