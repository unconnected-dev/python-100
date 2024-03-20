#Valid Sudoku
#https://leetcode.com/problems/valid-sudoku/description/
import math

caseBoard_1 = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
caseBoard_2 = [["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
caseBoard_3 = [[".",".",".",".","5",".",".","1","."],[".","4",".","3",".",".",".",".","."],[".",".",".",".",".","3",".",".","1"],["8",".",".",".",".",".",".","2","."],[".",".","2",".","7",".",".",".","."],[".","1","5",".",".",".",".",".","."],[".",".",".",".",".","2",".",".","."],[".","2",".","9",".",".",".",".","."],[".",".","4",".",".",".",".",".","."]]

if False:
    def isValidSudoku(board):
        all_columns = {}
        for i in range(1,10):
            all_columns[f'col_dict_{i}'] = {}

        all_squares = {}
        for i in range(1,4):
            for j in range(1,4):
                all_squares[f'square_dict_{i}_{j}'] = {}

        for i in range(len(board)):
            row_dict = {}
            for j in range(len(board[i])):
                val = board[i][j]
                if val != "." and val in row_dict:
                    return False
                else:
                    row_dict[val] = 1

                if val != "." and val in all_columns[f'col_dict_{j+1}']:
                    return False
                else:
                    all_columns[f'col_dict_{j+1}'][val] = 1

                sx = math.floor(i/3) + 1
                sy = math.floor(j/3) + 1
                if val != "." and val in all_squares[f'square_dict_{sx}_{sy}']:
                    return False
                else:
                    all_squares[f'square_dict_{sx}_{sy}'][val] = 1

        return True

if True:
    def isValidSudoku(board):
        all_cols = {}
        for i in range(9):
            all_cols[f"col_set_{i}"] = set()

        all_squares = {}
        for i in range(3):
            for j in range(3):
                all_squares[f'square_set_{i}_{j}'] = set()

        for r in range(9):
            print(board[r])

            row_set = set()
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
            
                if val in row_set:
                    print(f"row_set: {val}")
                    return False
                else:
                    row_set.add(val)
                
                if val in all_cols[f"col_set_{c}"]:
                    print(f"col_set_{c}: {val}")
                    return False
                else:
                    all_cols[f"col_set_{c}"].add(val)


                sx = math.floor(r/3)
                sy = math.floor(c/3)
                if val in all_squares[f"square_set_{sx}_{sy}"]:
                    return False
                else:
                    all_squares[f"square_set_{sx}_{sy}"].add(val)
        
        return True

print(f"{isValidSudoku(caseBoard_1)}")
print(f"{isValidSudoku(caseBoard_2)}")
print(f"{isValidSudoku(caseBoard_3)}")