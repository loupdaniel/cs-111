
def encode(text:str) -> str:
    '''
        INPUT:
            text --- the text to encode 

        OUTPUT:
            the encoded text
    '''

    # your favorite encoding method here!

    return text



def decode(text:str) -> str:
    '''
        INPUT:
            text --- the text to decode 

        OUTPUT:
            the decoded text
    '''

    # your favorite decoding method (for the encoding chosen) here!

    return text



def writeDiary(text) -> None:
    '''
        INPUT: 
            text --- text to write in diary

        SIDE EFFECT:
            text is written to new diary entry

        PRECONDITION:
            this function must be called from a folder 
            containing the folder "secret" 
            which contains the file "diary.txt"
    '''
    with open("secret/diary.txt", "a") as file:
        file.write(encode(text) + "\n")


def readDiary() -> str:
    '''
        OUTPUT: 
            contents of diary

        PRECONDITION:
            this function must be called from a folder 
            containing the folder "secret" 
            which contains the file "diary.txt"
    '''
    with open("secret/diary.txt", "r") as file:
        return decode(file.read())