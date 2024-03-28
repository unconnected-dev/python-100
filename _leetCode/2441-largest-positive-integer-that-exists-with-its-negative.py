#Largest Positive Integer That Exists With Its Negative
#https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/description/

caseNums_1 = [-1,2,-3,3]
caseNums_2 = [-1,10,6,7,-7,1]
caseNums_3 = [-10,8,6,7,-2,-3]

if False:
    def findMaxK(nums):
        nums.sort(reverse=True)

        for i in range(len(nums)):
            if nums[i] * -1 in nums:
                return nums[i]
        
        return -1
    
if False:
    def findMaxK(nums):
        my_set = set(nums)
        my_nums = list(my_set)
        my_nums.sort(reverse=True)

        for n in my_nums:
            if n*-1 in my_nums:
                return n
        
        return -1

if True:
    def findMaxK(nums):
        nums.sort(reverse=True)
        pos, neg = 0, len(nums) - 1

        while pos < neg:
            if nums[pos] == -nums[neg]:
                return nums[pos]
            elif nums[pos] > -nums[neg]:
                pos += 1
            else:
                neg -= 1

        return -1

print(f"{findMaxK(caseNums_1)}")
print(f"{findMaxK(caseNums_2)}")
print(f"{findMaxK(caseNums_3)}")