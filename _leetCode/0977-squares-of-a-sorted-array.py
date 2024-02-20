#Squares Of A Sorted Array
#https://leetcode.com/problems/squares-of-a-sorted-array/description/

caseNums_1 = [-4,-1,0,3,10]
caseNums_2 = [-7,-3,2,3,11]

if False:
    def sortedSquares(nums):
        return sorted([n**2 for n in nums])

if True:
    def sortedSquares(nums):
        left = 0
        right = len(nums) - 1
        result = []

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result.append(nums[left]**2)
                left += 1
            else:
                result.append(nums[right]**2)
                right -= 1
        
        return result

print(f"{sortedSquares(caseNums_1)}")
print(f"{sortedSquares(caseNums_2)}")