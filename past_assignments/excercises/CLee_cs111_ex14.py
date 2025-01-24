"""
Purpose: Solution for exercise 5.5.9
Author: Chanhui Lee
Date: October 11th, 2024
CS 111, Fall 2024
"""

def assignGP(score):
    """Assign a grade point to a score between 0 and 100."""
    
    if not isinstance(score, int) and not isinstance(score, float):
        return False
    
    if score >= 90:
        return 4
    if score >= 80:
        return 3
    if score >= 70:
        return 2
    if score >= 60:
        return 1
    return 0


def test_assignGP():
    """
    Runs unit tests for testing the assignGP function.
    
    Parameters:
        None
        
    Returns:
        Prints "Passed all unit tests!" if all test cases pass, 
        otherwise shows an AssertionError with a relevant error message.
    """
    assert assignGP(99) == 4, "Test case 1 failed"
    assert assignGP(89) == 3, "Test case 2 failed"
    assert assignGP(79) == 2, "Test case 3 failed"
    assert assignGP(69) == 1, "Test case 4 failed"
    assert assignGP(59) == 0, "Test case 5 failed"
    assert assignGP(90) == 4, "Test case 6 failed"
    assert assignGP(80) == 3, "Test case 7 failed"
    assert assignGP(70) == 2, "Test case 8 failed"
    assert assignGP(60) == 1, "Test case 9 failed"
    assert assignGP(100) == 4, "Test case 10 failed"
    assert assignGP(0) == 0, "Test case 11 failed"
    assert assignGP(-1) == 0, "Test case 12 failed"
    assert assignGP("-1") == False, "Test case 13 failed"
    assert assignGP(["abc", " ", "123.45"]) == False, "Test case 14 failed"
    print("Passed all unit tests!")


test_assignGP()
