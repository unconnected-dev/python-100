#Array Partition
#https://leetcode.com/problems/array-partition/description/

caseNums_1 = [1,4,3,2]
caseNums_2 = [6,2,6,5,1,2]

if False:
    def arrayPairSum(nums):
        nums = sorted(nums)
        total = 0
        for i in range(0, len(nums), 2):
            total += nums[i]

        return total

if True:
    def arrayPairSum(nums):
        nums.sort()
        return sum(nums[::2])
        
print(f"{arrayPairSum(caseNums_1)}")
print(f"{arrayPairSum(caseNums_2)}")