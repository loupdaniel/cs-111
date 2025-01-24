"""
Purpose: Solution for exercise 4.1.7
Author: Chanhui Lee
Date: September 18th, 2024
CS 111, Fall 2024
"""

def triangle(totalRows):
    """Prints out a triangle of any size using the symbol *.
    
    Parameters:
        totalRows: the total number of rows.
    
    Return value:
        None
    """
    
    for rowNum in range(totalRows): # print out the symbol * as much as the value of rowNum during the iteration.
        rowNum = rowNum + 1         # increment the value rowNum by 1 before printing out the symbol *.
        print("*" * rowNum)

triangle(10)