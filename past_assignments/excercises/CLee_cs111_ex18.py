#Your code goes between the lines of =======
#===================================================================================
"""
Purpose: Solution for exercise 18
Author: Chanhui Lee
Date: October 31st, 2024
CS 111, Fall 2024
"""
def wordCount(fileName):
    """Returns the number of words in the input file.

    Parameters:
        fileName: the name of the input file.

    Returns:
        the number of words in the input file.
    """
    
    textFile = open(fileName, 'r')
    
    result = textFile.read() # store strings in the file to the result variable
    
    result = result.split() # split the strings to list constituted with words
    
    return len(result)



fileName = "CS-111/text.txt"

def addAndRemember(a, b, remember):
    """A function whether returns the sum of a and b or the sum of the arguments from
    the previous time addAndRemember was called depending on whether remember is true or false.

    Parameters:
        a: a given integer.
        b: a given integer.
        remember: a flag variable for determining whether to return current sum or previous sum.

    Returns:
        result: either a current sum or a previous sum.
    """
    
    result = 0
    newResult = 0
    
    if remember == False:
        
        result += (a+b)
        
        tempFile = open(fileName, 'w')
        tempFile.write(str(result))
        tempFile.close()
        
        return result
    
    if remember == True:
        
        tempFile = open(fileName, 'r')
        result = int(tempFile.read()) # store the previous sum to return it
        tempFile.close()
        
        newResult += (a+b)
        tempFile = open(fileName, 'w')
        tempFile.write(str(newResult)) # overwrite the file with new sum
        tempFile.close()
        
        return result
    


check_wordCount = True
check_addAndRemember = True

#===================================================================================
# you should only edit this file above this line
# do not touch below this line

if check_wordCount:
    import os

    fileName = "temp.txt"

    while os.path.exists(fileName):
        fileName = "temp" + fileName

    tests = [
        "hi",
        "hello world",
        "my name is",
        "don't forget to breathe",
        "fair college on the hill",
        "to be or not to be"
    ]

    for i in range(len(tests)):
        with open(fileName, "w") as file:
            file.write(tests[i])
        count = wordCount(fileName)
        os.remove(fileName)
        assert count == i + 1, "Your wordCount implementation says there are " + str(count) + " words in: " + tests[i]
    print("\nYour wordCount implementation passes all tests. Great!")

if check_addAndRemember:
    tests = [
        (1,2,False,3),
        (5,7,True,3),
        (3,-3,True,12),
        (4,2,False,6),
        (8,9,True,6)
    ]
    for t in tests:
        ret = addAndRemember(t[0],t[1],t[2])
        msg = "Your addAndRemember implementation returns " + str(ret) + " for arguments " + str(t[0]) + ", " + str(t[1]) + ", and " + str(t[2]) + ", but the expected return was " + str(t[3])
        assert ret == t[3], msg
    print("\nYour repeats implementation passes all tests. Great!")


print()