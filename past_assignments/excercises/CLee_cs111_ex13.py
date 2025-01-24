"""
Purpose: String to Integer Converter
Author: Chanhui Lee
Date: October 10th, 2024
CS 111, Fall 2024
"""
def strToInt(s):
    """
    Converts a string to an integer.

    Parameter:
        s: a string

    Returns:
        - The integer value if conversion is successful.
        - False if conversion fails.
    """

    # Check if s is a string
    if not isinstance(s, str):
        return False

    # Try converting the string to an integer
    try:
        result = int(s)
        return result
    except ValueError:
        return False


def test_strToInt():
    assert strToInt("5") == 5
    assert strToInt(5) == False
    assert strToInt("1234567890") == 1234567890
    assert strToInt(["abc", " ", "123.45"]) == False
    print("Passed all unit tests!")

#test_strToInt()
print(strToInt("5.9"))

"""
Purpose: Solution for exercise 5.5.15
Author: Chanhui Lee
Date: October 10th, 2024
CS 111, Fall 2024
"""

def daysAlive():
    """
    Let the user to input their age and calculates the approximate number of days they have been alive.

    Parameters:
        None

    Returns:
        None
    """
    good = False
    text = input('How old are you? ')
    
    while not good:
        try:
            age = int(text)
            print('You have been alive for', round(age * 365.25), 'days!')
        except ValueError:
            return False
        else:
            good = True
            
#daysAlive()