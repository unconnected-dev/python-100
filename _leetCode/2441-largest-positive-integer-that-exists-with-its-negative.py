#Largest Positive Integer That Exists With Its Negative
#https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/description/

caseNums_1 = [-1,2,-3,3]
caseNums_2 = [-1,10,6,7,-7,1]
caseNums_3 = [-10,8,6,7,-2,-3]

if True:
    def findMaxK(nums):
        nums.sort(reverse=True)

        for i in range(len(nums)):
            if nums[i] * -1 in nums:
                return nums[i]
        
        return -1