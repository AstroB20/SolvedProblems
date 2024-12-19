def isValidSudoku(board:list):
    # def isRowValid(board):
    #     vals=["1","2","3","4","5","6","7","8","9"]
    #     for i in range(9):
    #         for j in range(9):
    #             ct=board[i].count(vals[j])
    #             if ct>1:
    #                 return False
    # if isRowValid(board)==False:
    #     return False
    # colBoard=[]
    # for i in range(9):
    #     ls=[]
    #     for j in range(9):
    #         ls.append(board[j][i])
    #     colBoard.append(ls)
    # if isRowValid(colBoard):
    #     return False
    colBoard=[]
    col,row=2,2
    while col<9:
        colBoard.append(board[0:col][0:row])
        col+=3
        row+=3
    return col

    
        
print(isValidSudoku([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,["5","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))

