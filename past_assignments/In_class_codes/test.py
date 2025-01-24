

def dbl(x):

    last = x[-1]*2  
    dblRest = []
    

    if len(x) == 1:

        dblRest.append(last)
        return dblRest
    else:

        dblRest = dbl(x[:-1])
        
        
        if len(x) > 1:

            dblRest.append(x.pop(-1)*2)
        else:

            dblRest.append(last)
        
        return dblRest


print(dbl([1,2,3]))
print(dbl([5]))
print(dbl([2,4,6,8]))
