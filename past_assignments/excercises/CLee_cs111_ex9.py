#Your code goes between the lines of =======
#===================================================================================
def removeNegatives(numList):
    """
    Removes negative numbers from a list of integers.

    Parameters:
        numList: A list of integers.

    Return value:
        A new list containing only the non-negative integers from the original list.
    """
    newList = []  # Initialize the accumulator list
    #for num in numList:
    #    if num >= 0:
    #        newList.append(num)
    #return newList
    index = 0

    while index < len(numList[index]):
        if numList[index] >= 0:
            newList.append(numList[index])
        index += 1
    return newList


def isPrime(num):
    """
    Determines if a number is prime or not.

    Args:
        num: An integer at least 2.

    Returns:
        True if the number is prime, False otherwise.
    """
    if num < 2:
        print("The input must be an integer at least 2.")

    check_isPrime = True  # Initialize the flag as True

    for i in range(2, num):
        if num % i == 0:
            check_isPrime = False
    return check_isPrime


check_removeNegatives = True # change this to True when you want to check removeNegatives
check_isPrime = True # change this to True when you want to check isPrime


#===================================================================================
# you should only edit this file above this line
# do not touch below this line

if check_isPrime:
    assert not isPrime(9), "Your code thinks 9 is prime, but it is divisible by 3."
    assert isPrime(2), "Your code thinks 2 is not prime when it is."
    assert isPrime(17), "Your code thinks 17 is not prime when it is."
    assert not isPrime(57), "Your code thinks 57 is prime, but it is divisible by 3."
    assert not isPrime(187), "Your code thinks 187 is prime, but it is divisible by 11."
    assert not isPrime(2093), "Your code thinks 2093 is prime, but it is divisible by 7."
    assert isPrime(8581), "Your code thinks 8581 is not prime when it is."
    assert not isPrime(879017), "Your code thinks 879017 is prime, but it is divisible by 887."
    assert isPrime(65537), "Your code thinks 65537 is not prime when it is."
    print("\nisPrime passes all tests. Great!")

if check_removeNegatives:
    assert removeNegatives([]) == [], "Your code does not return the empty list when given the empty list."
    assert -1 not in removeNegatives([-1]), "Your code does not remove -1 from [-1], but -1 < 0."
    assert 2 in removeNegatives([-10,-4,-37,2,-500]), "Your code removed 2 from [-10,-4,-37,2,-500], but 2 >= 0."
    assert len(removeNegatives([5,5,5,5,5])) == 5, "Your code seems to have changed the number of elements from 5 in [5,5,5,5,5]."
    assert len(removeNegatives([6,-17,9,-4,100,-43])) == 3, "Your code has not removed exactly 3 elements from [6,-17,9,-4,100,-43]."
    assert removeNegatives([-502, 0, -37, 0]) == [0,0], "Your code has not left the 0s in from [-502, 0, -37, 0]."
    print("\nremoveNegatives passes all tests. Great!")

print()