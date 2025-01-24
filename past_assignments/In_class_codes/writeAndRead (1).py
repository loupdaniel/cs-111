
fileName = "scrapFiles/text.txt"
#note: requires the folder scrapFiles to exist

def writeText(text:str) -> None:
    '''
        INPUT:
            text --- the text to write to the file

        SIDE EFFECT:
            the text is written to scrapFiles/text.txt

        OUTPUT: 
            None
    '''
    file = open(fileName, "w")
    file.write(text)
    file.close()


def readText() -> str:
    '''
        INPUT:
            None

        OUTPUT: 
            the contents of scrapFiles/text.txt
    '''
    file = open(fileName, "r")
    out = file.read()
    file.close()
    return out


writeText("hello")
print(readText())