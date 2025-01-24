#Your code goes between the lines of =======
#===================================================================================

def wordCount(fileName:str) -> int:
    '''
        INPUT:
            fileName -- the file to read the wordcount from

        OUTPUT:
            the number of words in fileName

        PRECONDITION:
            fileName exists in the current folder
            or is a path from the root (/) to an existing file
    '''

    with open(fileName, "r") as file:
        return len(file.read().split(" "))


def addAndRemember(a:int, b:int, remember:bool) -> int:
    '''
        INPUTS:
            a -- the first number to add
            b -- the second number to add 
            remember -- whether the previous sum should 
                be returned instead of the current sum

        OUTPUT:
            the sum of a and b if remember is false 
            or the sum from the previous call if 
            remember is true

        PRECONDITION:
            the folder tempFiles exists in the current folder
            and does not contain the file temp.txt
    '''

    fileName = "tempFiles/temp.txt" # where sum gets saved

    ret = a + b # will be replaced if remember is true
    if remember:
        with open(fileName, "r") as file:
            ret = int(file.read())
    
    # now to save the sum
    with open(fileName, "w") as file:
        file.write(str(a + b))

    return ret







check_wordCount = False
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