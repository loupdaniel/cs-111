
def printGrid(grid:list[list]) -> None:
    '''
        INPUT: 
            grid -- a 2D list
        
        SIDE EFFECT:
            grid gets printed nicely
    '''
    print()
    for row in grid:
        toPrint = ""
        for col in row:
            toPrint += str(col) + "\t"
        print(toPrint)
    print()



grid = [ 
    [0,0,1], 
    [0,1,0], 
    [1,0,0],
]
#print(grid)
#printGrid(grid)


ticTacToe = [
    ["x", "o", " "],
    ["o", "o", "x"],
    ["o", "x", "x"]
]

ticTacToe[0][2] = "x"


def checkDiag(grid:list[list]) -> bool:
    return False


def check4win(grid:list[list]) -> bool:

    #check rows 
    for row in grid:
        symbol = row[0]

        won = True

        for col in row:
            if col != symbol:
                won = False

        if won:
            return True


    #check columns 

    for coli in range(len(grid[0])):

        won = True 

        symbol = grid[0][coli]

        for row in grid:
            
            if row[coli] != symbol:
                won = False 
    
        if won:
            return True
        

    #check diagonals
    return checkDiag(grid)



grid = [
    [1,0,0,0],
    [0,1,1,1],
    [1,1,0,0],
    [0,1,0,1]
]

#res = check4win(grid)
#print(res)
