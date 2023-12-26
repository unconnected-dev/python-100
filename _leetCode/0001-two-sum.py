#Two Sum
#https://leetcode.com/problems/two-sum/description/

caseNums_1 = [2,7,11,15]
caseTarget_1 = 9

caseNums_2 = [3,2,4]
caseTarget_2 = 6

caseNums_3 = [3,3]
caseTarget_3 = 6

#Stores dictionary of the numbers as loops through once
#Checks against that dictionary for the second number that adds to target
if False:
    def twoSum(nums, target):
        storedIndicies = dict()

        for key, num in enumerate(nums):
            target_minus_num = target - num

            if target_minus_num in storedIndicies:
                return [key, storedIndicies[target_minus_num]]
            else:
                storedIndicies[num] = key

#Double loops through the nums
if True:
    def twoSum(nums, target):
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]

print(f"{twoSum(caseNums_1, caseTarget_1)}")    
print(f"{twoSum(caseNums_2, caseTarget_2)}")    
print(f"{twoSum(caseNums_3, caseTarget_3)}")    