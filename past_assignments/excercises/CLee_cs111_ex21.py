#Your code goes between the lines of =======
#===================================================================================

def getLetterCount(text:str):
    """A function which takes a string and returns the a dictionary which gives the count of each character in the string.

    Parameters:
        text:  a string.
        
    Returns:
        resDict: a dictionary which gives the count of each character in the string.
    """
    
    resDict = {}
    
    # hello
    for i in range(len(text)):
        
        if text[i] in resDict:
            continue
        
        count = 1
        
        for j in range(1, len(text) - i):
            
            if text[i] == text[i+j]:
                count += 1
           
        resDict[text[i]] = count
    
    return resDict

# print(getLetterCount("hello"))



def toAssociationList(d):
    """A function turns a dictionary into an association list.

    Parameters:
        d:  a dictionary.
        
    Returns:
       result: a list of 2-element tuples, each of which is a key-value pair from the dictionary.
    """

    keyList = list(d.keys())
    valList = list(d.values())
    result = []
    
    for i in range(len(d)):
        result.append((keyList[i], valList[i]))
    
    return result


# print(toAssociationList({"h":1, "e":1, "l":2, "o":1}) )


check_getLetterCount = True
check_toAssociationList = True

#===================================================================================
# you should only edit this file above this line
# do not touch below this line

import random, string

if check_getLetterCount:
    tests = [
        "hello",
        "how are you?",
        "is it me you're looking for?",
        "",
        "123546789012345678901234567890",
        string.ascii_letters,
        string.whitespace
    ]
    for t in tests:
        result = getLetterCount(t)
        for letter in t:
            assert letter in list(result.keys()), "Your getLetterCount implementation does not have an entry for the letter \"" + letter + "\" when run on \"" + t + "\""
            assert result[letter] == t.count(letter), "Your getLetterCount implementation says there are " + str(result[letter]) + " instances of  \"" + letter + "\" when run on \"" + t + "\""
        for k in list(result.keys()):
            assert k in t, "Your getLetterCount implementation has an entry for the letter \"" + k + "\" when run on \"" + t + "\""
    print("\nYour getLetterCount implementation passes all tests. Great!")

if check_toAssociationList:
    for i in range(100):
        acc = {}
        for letter in string.ascii_letters:
            acc[letter] = random.randint(0,100)
        aList = toAssociationList(acc)
        for kv in aList:
            assert acc[kv[0]] == kv[1], "Your toAssociationList implementation pairs the key " + str(kv[0]) + " with the value " + str(kv[1]) + " when it should be paired with " + str(acc[kv[0]])
        for k in string.ascii_letters:
            found = False
            for kv in aList:
                if kv[0] == k:
                    found = True 
            assert found, "Your toAssociationList implementation is missing an entry for the key \"" + k + "\""
    print("\nYour toAssociationList implementation passes all tests. Great!")

print()