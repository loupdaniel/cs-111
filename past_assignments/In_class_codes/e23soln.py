#Your code goes between the lines of =======
#===================================================================================


def checkDiag(grid:list[list]) -> bool:
    '''
        INPUT:
            grid -- a 2D list 
        
        OUTPUT:
            a bool indicating whether either diagonal 
            of the list has all the same elements

        PRECONDITION:
            grid has an equal number of rows and columns
    '''

    length = len(grid)

    # check upper left to lower right
    symbol = grid[0][0]
    won = True

    for i in range(length):

        if grid[i][i] != symbol:
            won = False 

    if won:
        return True 
    

    # check lower left to upper right
    symbol = grid[length-1][0]
    won = True 

    for i in range(length):

        if grid[length-1-i][i] != symbol:
            won = False 

    return won
        



def neighbors(grid:list[list[int]], row:int, col:int) -> list[int]:
    '''
        INPUTS:
            grid -- a 2D grid
            row -- the row index 
            col -- the column index

        OUTPUT:
            a list of neighbors of the row,col element

        PRECONDITION:
            row, col is a grid element
    '''
    out = []

    if row >= 1:
        out.append(grid[row-1][col])

    if row < len(grid) - 1:
        out.append(grid[row+1][col])

    if col >= 1:
        out.append(grid[row][col-1])

    if col < len(grid[0]) - 1:
        out.append(grid[row][col+1])

    return out




check_checkDiag = True  
check_neighbors = True

#===================================================================================
# you should only edit this file above this line
# do not touch below this line

if checkDiag:
    ullr = [
        [
            [5,7,6],
            [4,5,3],
            [2,1,5]
        ],
        [
            [
                [1,0,0,0,0],
                [0,1,0,0,0],
                [0,0,1,0,0],
                [0,0,0,1,0],
                [0,0,0,0,1]
            ]
        ],
        [[0]]
    ]
    for g in ullr:
        assert checkDiag(g), "Your checkDiag implementation doesn't find the upper-left-to-lower-right diagonal in " + str(g)

    llur = [
        [
            [0,1,1],
            [1,1,0],
            [1,0,0]
        ],
        [
            [0,1],
            [1,1]
        ]
    ]
    for g in llur:
        assert checkDiag(g), "Your checkDiag implementation doesn't find the lower-left-to-upper-right diagonal in " + str(g)

    noDiag = [
        [
            [1,2],
            [3,4]
        ],
        [
            [0,0,0],
            [0,1,0],
            [0,0,0]
        ],
        [
            [0,0,1],
            [0,0,0],
            [0,0,1]
        ],
        [
            [1,0,0],
            [0,0,0],
            [1,0,0]
        ],
        [
            [1,0,1],
            [0,0,0],
            [0,0,0]
        ],
        [
            [0,0,0],
            [0,0,0],
            [1,0,1]
        ]
    ]
    for g in noDiag:
        assert not checkDiag(g), "Your checkDiag implementation mistakenly says there is a diagonal in " + str(g)

    print("\nYour checkDiag implementation passes all tests. Congrats!")
    

if check_neighbors:
    g = [
        [0, 1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10,11],
        [12,13,14,15,16,17]
    ]

    tests = [
        (1,3,[3,8,10,15]),
        (1,0,[0,7,12]),
        (2,1,[12,7,14]),
        (2,5,[16,11])
    ]

    for t in tests:
        ns = neighbors(g,t[0],t[1])
        for i in range(18):
            if i in t[2]:
                assert i in ns, "missing neighbor " + str(i) + " for " + str(g[t[0]][t[1]]) + " in " + str(g)
            else:
                assert i not in ns, "non-neighbor " + str(i) + " given for " + str(g[t[0]][t[1]]) + " in " + str(g)

        assert len(ns) == len(t[2]), "neighbors returns the wrong number of neighbors for " + str(g[t[0]][t[1]]) + " in " + str(g)

    print("\nYour neighbors implementation passes all tests. Congrats!")


print()