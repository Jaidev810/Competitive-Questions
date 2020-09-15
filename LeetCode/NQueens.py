def isSafe(row, col, board, n):

    i = row-1
    while i >= 0:
        if board[i][col] == 'Q':
            return False
        i -= 1
        
    i = row-1
    j = col-1

    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    i = row-1
    j = col+1

    while i >= 0 and j < n:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    return True

def printNhelper(row, n, board):
    if row == n:
        return board
    
    for i in range(0, n):
        if isSafe(row, i, board, n):
            board[row][i] = 'Q'
            printNhelper(row+1, n, board)
            board[row][i] = '.'
    return board

    

def printQueens(n):
    board = [['.' for i in range(n)] for j in range(n)]
    arr = printNhelper(0, n, board)
    return arr



n = int(input())
arr = printQueens(n)
print(arr)