#Matrix Diagonal Sum
#https://leetcode.com/problems/matrix-diagonal-sum/description/

caseMat_1 = [[1,2,3],[4,5,6],[7,8,9]]
caseMat_2 = [[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]
caseMat_3 = [[5]]

if False:
    def diagonalSum(mat):
        total = 0

        for i in range(0, len(mat)):
            total += mat[i][i]

        j = 0
        for i in range(len(mat)-1, -1, -1):
            total += mat[i][j]
            j+=1

        if len(mat) % 2 != 0:
            mid = (len(mat)//2)
            total -= mat[mid][mid]

        return total

if True:
    def diagonalSum(mat):
        total = 0
        total += sum([mat[i][i] for i in range(0, len(mat))])
        total += sum(mat[i][j] for i, j in zip(range(len(mat)-1, -1, -1), range(len(mat))))

        if len(mat) % 2 != 0:
            mid = (len(mat)//2)
            total -= mat[mid][mid]
        
        return total

print(f"{diagonalSum(caseMat_1)}")
print(f"{diagonalSum(caseMat_2)}")
print(f"{diagonalSum(caseMat_3)}")