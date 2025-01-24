    

def searchWhile(lst:list[int], target:int) -> bool:
    '''
        INPUTS:
            lst -- the list to search 
            target -- the number to search for in lst

        OUTPUT:
            whether lst contains target 
    '''

    i = 0
    found = False

    while i < len(lst):
        found = found or lst[i] == target
        i += 1

    return found



def searchRec(lst:list[int], target:int) -> bool:
    '''
        INPUTS:
            lst -- the list to search 
            target -- the number to search for in lst

        OUTPUT:
            whether lst contains target 
    '''

    def searchHelper(i:int) -> bool:
        '''
            INPUT:
                i -- the index searched up to

            OUTPUT:
                whether lst contains target 
                at index i or above
        '''

        if i < len(lst):
            return lst[i] == target or searchHelper(i+1)
        else:
            return False
        
    return searchHelper(0)
    



import random

for i in range(100):

    lst = [] 
    for j in range(50):
        lst.append(random.randint(0,100))

    target = random.randint(0,100)
    
    assert searchRec(lst, target) == searchWhile(lst, target)

print("\nThey match!\n")