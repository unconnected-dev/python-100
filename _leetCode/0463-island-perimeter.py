#Island Perimeter
#https://leetcode.com/problems/island-perimeter/description/

caseGrid_1 = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
caseGrid_2 = [[1]]
caseGrid_3 = [[1,0]]
caseGrid_4 = [[0,1]]

if False:
    #This does not work for case 4
    def islandPerimeter(grid):
        total = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    total += 4

                    #Check left
                    if i > 0 and grid[i - 1][j] == 1:
                        total -= 1
                    #Check right
                    if i < len(grid) - 1 and grid[i + 1][j] == 1:
                        total -= 1
                    #Check top
                    if j > 0 and grid[i][j - 1] == 1:
                        total -= 1
                    #Check bottom
                    if j < len(grid[j]) - 1 and grid[i][j + 1] == 1:
                        total -= 1
        
        return total

if True:
    def islandPerimeter(grid):
        total = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):

                if grid[i][j] == 1:
                    total += 4
                    #Left
                    if i > 0 and grid[i-1][j] == 1:
                        total -= 2
                    #Top
                    if j > 0 and grid[i][j-1] == 1:
                        total -= 2
        return total
    
print(f"{islandPerimeter(caseGrid_1)}")
print(f"{islandPerimeter(caseGrid_2)}")
print(f"{islandPerimeter(caseGrid_3)}")
print(f"{islandPerimeter(caseGrid_4)}")