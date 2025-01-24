import random 




def randomish():
    '''
        OUTPUT: a "random" number between 
            1 and 100 inclusive
    '''

    random.seed(111)

    return random.randint(1,100)


for i in range(10):
    print(randomish())