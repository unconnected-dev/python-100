#Delete Greatest Value In Each Row
#https://leetcode.com/problems/delete-greatest-value-in-each-row/description/

caseGrid_1 = [[1,2,4],[3,3,1]]
caseGrid_2 = [[10]]

if True:
    def deleteGreatestValue(grid):
        
        total = 0
        nl = []

        while len(grid[0]) > 0:
            for row in grid:
                highest = 0
                for n in row:
                    if n > highest:
                        highest = n

                row.remove(highest)
                nl.append(highest)

            total += max(nl)
            nl = []

        return total
    
print(f"{deleteGreatestValue(caseGrid_1)}")
print(f"{deleteGreatestValue(caseGrid_2)}")