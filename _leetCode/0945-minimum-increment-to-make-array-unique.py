#Minimum Increment To Make Array Unique
#https://leetcode.com/problems/minimum-increment-to-make-array-unique/description/

from collections import Counter


caseNums_1 = [1,2,2]
caseNums_2 = [3,2,1,2,1,7]

if True:
    def minIncrementForUnique(nums):
        
        if not nums:
            return 0
        
        nums.sort()
        res = 0
        prev = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] <= prev:
                prev += 1
                res += prev - nums[i]
            else:
                prev = nums[i]
                
        return res

print(f"{minIncrementForUnique(caseNums_1)}")
print(f"{minIncrementForUnique(caseNums_2)}")