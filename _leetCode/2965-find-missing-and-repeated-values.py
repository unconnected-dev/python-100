#Find Missing And Repeated Values
#https://leetcode.com/problems/find-missing-and-repeated-values/description/

caseGrid_1 = [[1,3],[2,2]]
caseGrid_2 = [[9,1,7],[8,9,2],[3,4,6]]

if False:
    def findMissingAndRepeatedValues(grid):
        grid_length = len(grid)
        row_length = len(grid[0])

        list_range = [i for i in range(1, (grid_length * row_length) + 1)]
        checked = []

        a = -1
        b = -1
        for row in grid:
            for n in row:
                if n in checked: 
                    a = n
                checked.append(n)

        for i in list_range:
            if i not in checked:
                b = i
                break

        return [a,b]

if True:
    def findMissingAndRepeatedValues(grid):
        checked = []

        a, b = -1, -1
        for row in grid:
            for n in row:
                if n in checked: 
                    a = n
                checked.append(n)

        for i in range(1, (len(grid) * len(grid[0])) + 1):
            if i not in checked:
                b = i
                break

        return [a,b]

print(f"{findMissingAndRepeatedValues(caseGrid_1)}")
print(f"{findMissingAndRepeatedValues(caseGrid_2)}")