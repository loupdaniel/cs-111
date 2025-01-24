"""
def ceaserEncode(text, shift):
textList = ""

for index in text:
    if ord(index) + shift > 122:
        textList += chr(ord("a") + shift - 1 - (ord("z") - ord(index)))
    
    elif ord(index) + shift > 90:
        textList += chr(ord("A") + shift - 1 - (ord("Z") - ord(index)))
    
    else:    
        textList += chr(ord(index)+shift)

return textList
"""

def ceasarEncode(text:str, shift:int) -> str:
    '''
        INPUT:
            text --- the text to be encoded 
            shift --- the amount to shift by

        PRECONDITION:
            text is made up of only lowercase letters

        OUTPUT:
            a Ceasar cipher encoded text 
    '''

    acc = ""

    offset = 97

    for letter in text:
        
        asciiNum = ord(letter)
        assert asciiNum >= offset and asciiNum < offset + 26

        position = asciiNum - offset

        acc += chr((position + shift) % 26 + offset)

    return acc


print(ceasarEncode("abc", 1))

print(ceasarEncode("abc", 2))

print(ceasarEncode("abcxyz",1))

print(ceasarEncode("abcxyz",-1))


def ceasarDecode(text:str, shift:int) -> str:
    '''
        INPUT:
            text --- the text to be encoded 
            shift --- the amount the text was shifted by

        PRECONDITION:
            text is made up of only lowercase letters

        OUTPUT:
            a Ceasar cipher decoded text 

        POSTCONDITION:
            ceaserDecode(ceasarEncode(text, shift), shift) == text
    '''
    return ceasarEncode(text, -shift)


print(ceasarDecode(ceasarEncode("abcxyz", 30), 30))