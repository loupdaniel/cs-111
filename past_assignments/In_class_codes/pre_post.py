


def funny(a:int, b:int, c:int) -> float:
    '''
        INPUTS:
            a,b,c --- some integers

        PRECONDITION:
            a + b != 0 

        OUTPUT:
            c/(a+b)
    '''
    
    assert a + b != 0, "Hey! a+b can't be 0!"

    return c / (a+b)






def padString(s:str, length:int) -> str:
    '''
        INPUTS:
            s --- the string to pad with spaces
            length --- the length to pad up to

        OUTPUT:
            a string t padded with spaces at the end

        POSTCONDITION:
            len(padString(s, length)) >= length
    '''

    while len(s) < length:
        s += " "    
    # now len(s) >= length
    
    return s