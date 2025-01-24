#Your code goes between the lines of =======
#===================================================================================
"""
Purpose: Solution for exercise 19
Author: Chanhui Lee
Date: November 1st, 2024
CS 111, Fall 2024
"""

def removeNumbers(wordList):
    """A function that deletes all of the words that begin with a digit from the list of words

    Parameters:
        wordList: the given list of words
        
    Returns:
        None
    """
    
    index = 0
    
    while index < len(wordList):
        word = wordList[index]
        
            
        try:
            int(word[0])
        except ValueError:      # catches ValueError when the word[0] is not a digit
            index = index + 1
        except IndexError:      # catches IndexError when the len(word) is 0
            index = index + 1
        else:
            wordList.pop(index)



#sampleList = ["", "4asdfa", "asdfa", "4asdf"]
#removeNumbers(sampleList)
#print(sampleList)



check_removeNumbers = True
check_sqList = False

#===================================================================================
# you should only edit this file above this line
# do not touch below this line

import string

def getNumber(words):
    ret = None
    for word in words:
        if len(word) > 0 and word[0] in string.digits:
            ret = word
    return ret

def checkOrder(arg, x):
    ordered = True
    for i in range(len(x) - 1):
        fst = x[i]
        snd = x[i+1]
        if arg.index(fst) > arg.index(snd):
            ordered = False 
    return ordered

if check_removeNumbers:
    tests = [
        ["hi"],
        ["hello", "world"],
        ["2cool"],
        ["1", "2", "3"],
        ["4","you"],
        [""],
        ["why", "was", "6", "afraid", "of", "7?"],
        ["because", "7", "8", "9"],
    ]
    for t in tests:
        x = t[:]
        try:
            res = removeNumbers(x)
        except IndexError:
            if len(t) > 0 and t[0] == "":
                assert False, "Your removeNumbers implementation tries to access an index that is out of range on input " + str(t) + ". Are you checking that the each string is nonempty before indexing into its first element? If not, you should be."
            else:
                assert False, "Your removeNumbers implementation tries to access an index that is out of range on input " + str(t) + ". Are you mutating the list while iterating over it? If so, think about how that might change the list's length and the list elements' indices. Then adjust your code's indexing accordingly. Consider using a while-loop."
        num = getNumber(x)
        assert res == None, "Your removeNumbers implementation isn't supposed to return anything, but it returns " + str(res) 
        assert num == None, "Your removeNumbers implementation does not remove " + num + " from " + str(t)
        for word in x:
            assert word in t, "Your removeNumbers implementation mistakenly removes " + word + " from " + str(t)
        assert checkOrder(t,x), "Your remove numbers implementation changes the order of " + str(t) + " to " + str(res) + ", but the order of remaining elements should not change."
    print("\nYour wordCount implementation passes all tests. Great!")

if check_sqList:
    for i in range(100):
        lst = sqList(i)
        acc = []
        for j in range(i):
            if j % 2 == 0:
                acc.append(j * j)
        assert len(lst) == len(acc), "Your sqList implementation does not yield the right number of elements for input " + str(i)
        for i in range(len(acc)):
            assert lst[i] == acc[i], "Your sqList implementation yields a " + str(lst[i]) + " where the expected number is " + str(acc[i]) 
    print("\nYour sqList implementation passes all tests. Great!")

print()