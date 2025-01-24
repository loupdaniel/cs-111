#Your code goes between the lines of =======
#===================================================================================


def getLetterCount(text:str) -> dict[str,int]:
    '''
        INPUT:
            text -- the string to get symbol counts for

        OUTPUT:
            a dictionary with keys that are symbols in text 
            and values that are the counts of those symbols
    '''
    acc = {}
    for letter in text:
        if letter in list(acc.keys()):
            acc[letter] += 1
        else:
            acc[letter] = 1
    return acc



def toAssociationList(d:dict[str,int]) -> list[tuple[str,int]]:
    '''
        INPUT:
            d -- a dictionary 

        OUTPUT:
            an association list representing d
    ''' 
    acc = []
    for k in list(d.keys()):
        acc.append((k,d[k]))
    return acc


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