#Your code goes between the lines of =======
#===================================================================================
def swap(word:str, index1:int, index2:int):
    """Returns the input word but with the characters at index1 and index2 swapped.

    Parameters:
        word: the input word.
        index1: the index number of index1.
        index2: the index number of index2.

    Return values:
        res: the new word with index1 and index2 swapped from the input word.
    """
    res = ""
    
    for index in range(len(word)):
        if index == index1:
           res += word[index2]
        
        elif index == index2:
           res += word[index1]
        
        else:
            res += word[index] 

    return res


# print(swap("coal",2,3))
# print(swap("david",1,3))

def pigLatin(text:str):
    """Returns the pig latin version of the input text.

    Parameters:
        text: the input text.

    Return values:
        res: the pig latin version of the input text.
    """
    
    res = ""
    wordList = []
    count = 0 # accumulator for the word count in the wordList
    
    wordList = text.split()
    
    for word in wordList:
        if word[0] in "aeiou":
            res += (word[1:len(word)] + "way")
        
        else:
            res += (word[1:len(word)] + word[0] + "ay")
        
        if count != len(wordList)-1:    # don't add a space if it's the last word of the wordList    
            res += " "
        
        count += 1
    
    return res

# print(pigLatin("to be or not to be"))
# print(pigLatin("denison"))
# print(pigLatin("university"))


check_swap = True
check_pigLatin = True

#===================================================================================
# you should only edit this file above this line
# do not touch below this line

if check_swap:
    assert swap("coal",2,3) == "cola", "Your swap function does not swap cola to coal with indices 2,3"
    assert swap("coal",3,2) == "cola", "Your swap function does not swap cola to coal with indices 3,2"
    assert swap("david",1,3) == "divad", "Your swap function does not swap david to divad"
    for i in range(len("hello")):
        assert swap("hello",i,i) == "hello", "Your swap function does keep hello the same when swapping the same character with itself"
    print("\nYour swap implementation passes all tests. Great!")

if check_pigLatin:
    tests = [
        ("denison", "enisonday"),
        ("university", "niversityway"),
        ("hello", "ellohay"),
        ("hello world", "ellohay orldway"),
        ("to be or not to be", "otay ebay rway otnay otay ebay")
    ]
    for arg,ret in tests:
        assert pigLatin(arg) == ret, "Your pigLatin function does not turn " + arg + " into " + ret
    print("\nYour pigLatin implementation passes all the tests. Great!")

print()