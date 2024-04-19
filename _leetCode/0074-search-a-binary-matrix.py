#Search A Binary Matrix
#https://leetcode.com/problems/search-a-2d-matrix/description/

caseMatrix_1 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
caseTarget_1 = 3

caseMatrix_2 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
caseTarget_2 = 13

caseMatrix_3 = [[1,3,5]]
caseTarget_3 = 1

if True:
    def searchMatrix(matrix, target):
        bottom, mid, top = 0, 0, len(matrix) - 1 

        while bottom <= top:
            mid = (top + bottom)//2

            if matrix[mid][0] <= target <= matrix[mid][len(matrix[mid])-1]:
                break
            elif matrix[mid][len(matrix[mid])-1] > target:
                top = mid - 1
            else:
                bottom = mid + 1

        left, mid_, right = 0, 0, len(matrix[mid]) - 1

        while left <= right:
            mid_ = (left + right)//2

            if matrix[mid][mid_] == target:
                return True
            elif matrix[mid][mid_] > target:
                right = mid_ - 1
            else:
                left = mid_ + 1
        
        return False

print(f"{searchMatrix(caseMatrix_1, caseTarget_1)}")
print(f"{searchMatrix(caseMatrix_2, caseTarget_2)}")
print(f"{searchMatrix(caseMatrix_3, caseTarget_3)}")
