
fileName = "scrapFiles/appendage.txt"
#note: requires the folder scrapFiles to exist

def appendText(text:str) -> None:
    '''
        INPUT:
            text --- the text to append to the file

        SIDE EFFECT:
            the text is appended to scrapFiles/text.txt

        OUTPUT: 
            None
    '''
    with open(fileName, "a") as file:
        file.write(text)

def readText() -> str:
    '''
        INPUT:
            None

        OUTPUT: 
            the contents of scrapFiles/text.txt 
            with newlines replaces with spaces
    '''
    with open(fileName, "r") as file:
        acc = ""
        for line in file:
            acc += line + " "
    return acc

for i in range(10):
    appendText(str(i))

print(readText())