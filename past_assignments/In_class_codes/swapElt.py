
def swapElt(lst:list, i1:int, i2:int) -> None:
    '''
        INPUTS:
            lst -- the list to mutate
            i1 -- the first index 
            i2 -- the second index

        SIDE EFFECT:
            lst is mutated to swap the elements
            at indices i1 and i2
    '''

    a = lst[i1]
    b = lst[i2]

    lst[i1] = b 
    lst[i2] = a



x = [1,2,3]
swapElt(x,0,1)
print(x)