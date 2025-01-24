#Your code goes between the lines of =======
#===================================================================================
def isPrime(num):
    """
    Determines if a number is prime or not.

    Parameters:
        num: An integer at least 2.

    Returns:
        True if the number is prime, False otherwise.
    """
    if num < 2:
        print("The input must be an integer at least 2.")

    check_isPrime = True  # Initialize the flag as True

    i = 2
    while i < num:
        if num % i == 0:
            check_isPrime = False
        i = i + 1
    return check_isPrime


def virus(rate, target):
    """
    Returns the number of days until target people are infected by a virus.

    Parameters:
        rate: The daily growth rate.
        target: The target number of infected people.

    Returns:
        The number of days until target people are infected.
    """
    
    days = 0
    totalInfected = 1
    while totalInfected < target:
        totalInfected = totalInfected * rate
        days = days + 1
    return days


check_isPrime = True # change this to True when you want to check isPrime
check_virus = True # change this to True when you want to check virus

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

if check_virus:
    assert virus(0.5, 1) == 0, "Your code doesn't think the first person is infected on day 0."
    assert virus(0.5, 10) == 6, "Your code doesn't think that the first day 10 people are infected with rate 0.5 is day 6."
    assert virus(2.7, 1000) == 6, "Your code doesn't think that the first day 1000 people are infected with rate 2.7 is day 6."
    assert virus(0.01, 123) == 484, "Your code doesn't think that the first day 123 people are infected with rate 0.01 is day 484."
    assert virus(0.3, 999999999) == 79, "Your code doesn't think that the first day 999999999 people are infected with rate 0.3 is day 79."
    print("\nvirus passes all tests. Great!")

print()