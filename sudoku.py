def main():
    # read 9x9 board from input
    board = [[int(c) if c.isdigit() else 0 for c in input()] for _ in range(9)]
    solve(board)
    
def solve(board, row=0, col=0):
    if row > 8:
        print_board(board)
        return
        
    nrow = row + (col+1)//9
    ncol = (col+1)%9

    if board[row][col] > 0:
        solve(board, nrow, ncol)
    else:
        for x in range(1, 10):
            board[row][col] = x
            if is_valid_board(board):
                solve(board, nrow, ncol)
            board[row][col] = 0

def is_valid_board(board):
    checks = []
    for row in board:
        checks.append(row)
    for col in range(9):
        checks.append([row[col] for row in board])
    for grid in range(9):
        row_min = grid // 3 * 3
        col_min = grid % 3 * 3
        checks.append([board[row][col] for row in range(row_min, row_min+3) for col in range(col_min, col_min+3)])
    for check in checks:        
        if has_dup(check):
            # print("Has dup")
            # print("Check", check)
            # print_board(board)                      
            return False
    return True

def has_dup(list):
    list = [ele for ele in list if ele != 0]
    return len(list) != len(set(list))                   

def print_board(board):
    for row in board:
        for c in row:
            print(c, end='')
        print()
    
if __name__ == "__main__":
    main()
