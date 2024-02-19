#Squares Of A Sorted Array
#https://leetcode.com/problems/squares-of-a-sorted-array/description/

caseNums_1 = [-4,-1,0,3,10]
caseNums_2 = [-7,-3,2,3,11]

if True:
    def sortedSquares(nums):
        return sorted([n**2 for n in nums])

print(f"{sortedSquares(caseNums_1)}")
print(f"{sortedSquares(caseNums_2)}")