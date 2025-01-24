#Your code goes between the lines of =======
#===================================================================================




def median(data:list[float]) -> float:
    '''
        INPUT:
            data -- list of numbers 

        OUTPUT:
            the median of data
    '''

    copy = data[:]
    copy.sort()
    length = len(copy)

    if length % 2 == 0:
        return (copy[length//2] + copy[length//2 -1]) / 2
    else:
        return copy[length//2]




def reverseSort(data:list[int]) -> None:
    '''
        INPUT:
            data -- list of numbers

        SIDE EFFECT:
            data becomes sorted descendingly
    '''

    data.sort()

    for i in range(len(data)//2):

        # now to just swap the front of the list with the back
        # to reverse everything
        temp = data[i]
        data[i] = data[-(i+1)]
        data[-(i+1)] = temp












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