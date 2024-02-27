#Largest Local Values In A Value
#https://leetcode.com/problems/largest-local-values-in-a-matrix/description/

caseGrid_1 = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]
caseGrid_2 = [[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]

if True:
    def largestLocal(grid):
        result = []
        
        #This gets top point
        for row in range(0, len(grid) - 2):
            result_row = []

            #This gets leftmost point            
            for col in range(0, len(grid[row]) - 2):

                high_val = 0
                #Go through 3x3 and get high value
                for i in range(row, row + 3):
                    for j in range(col, col + 3):
                        if grid[i][j] > high_val:
                            high_val = grid[i][j]
                
                result_row.append(high_val)
            
            result.append(result_row)

        return result

print(f"{largestLocal(caseGrid_1)}")
print(f"{largestLocal(caseGrid_2)}")