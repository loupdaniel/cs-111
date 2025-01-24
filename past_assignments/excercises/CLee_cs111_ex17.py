def encode(word:str) -> str:
    '''
        INPUT:
            word -- word to encode

        OUTPUT:
            encoded word with even indexed chars followed 
            by odd indexed chars
    '''
    evens = ""
    odds = ""

    for i in range(len(word)):

        if i % 2 == 0:
            evens += word[i]
        else:
            odds += word[i]

    return evens + odds

#Your code goes between the lines of =======
#===================================================================================

def decode(codeword):
    '''
        INPUT:
            codeword -- encoded word
            
        OUTPUT:
            plain text with characters in their original positions
    '''
    
    totalLen = len(codeword)
    evensLen = (totalLen + 1) // 2
    

    evens = codeword[:evensLen]
    odds = codeword[evensLen:]
    

    result = ""
    
    for i in range(totalLen):
        
        if i % 2 == 0:
            result += evens[i//2]
        else:
            result += odds[i//2]
            
    return result


def repeats(text):
    """Finds all consecutive repeated substrings in the given text.

    Parameters:
        text: The input string.

    Return values:
        result: A list of substrings that are repeated consecutively.
    """
    result = []
    n = len(text)
    
    for i in range(n):
        maxLenSub = (n - i) // 2
        
        for lenSub in range(1, maxLenSub + 1):
            firstSub = text[i:i + lenSub]
            secondSub = text[i + lenSub:i + 2 * lenSub]
            
            if firstSub == secondSub and firstSub not in result:
                result.append(firstSub)
    
    return result


check_decode = True
check_repeats = True

#===================================================================================
# you should only edit this file above this line
# do not touch below this line

if check_decode:
    tests = ["computers", "python", "denison", "university", "a"]
    for t in tests:
        assert decode(encode(t)) == t, "Your decode implementation does not decode the encoding of " + t + " properly"
    print("\nYour decode implementation passes all tests. Great!")

if check_repeats:
    tests = [
        ("hello", ["l"]),
        ("I think that hat is cool", ["hat ", "o"]),
        ("aabbcc", ["a", "b", "c"]),
        ("I think that that is spiffy", [" that", "that ", "f"])
    ]
    for t in tests:
        ret = repeats(t[0])
        assert ret == t[1], "Your repeats implementation returns " + str(ret) + " for \"" + str(t[0]) + "\" but the expected return was " + str(t[1])
    print("\nYour repeats implementation passes all tests. Great!")


print()