#3Sum
#https://leetcode.com/problems/3sum/description/

from typing import List


caseNums_1 = [-1,0,1,2,-1,-4]
caseNums_2 = [0,1,1]
caseNums_3 = [0,0,0]
caseNums_4 = [-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]

if False:
    def threeSum(nums) -> List[List[int]]:
        i = 0
        nums = sorted(nums)
        
        if len(nums) <= 2:
            return []
        
        res = {}
        while i <= len(nums) - 2:
            start_val = nums[i]
            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[left] + nums[right]
                if start_val + total == 0:
                    res[f"{start_val}_{nums[left]}_{nums[right]}"] = [start_val, nums[left], nums[right]] 
                    left += 1
                elif start_val + total < 0:
                    left += 1
                elif start_val + total > 0:
                    right -= 1

                if ((start_val + nums[left]) > nums[right]) or (start_val == 0 and nums[left] == 0 and nums[right] == 0):
                    if left < right and start_val + nums[left] + nums[right] == 0:
                        res[f"{start_val}_{nums[left]}_{nums[right]}"] = [start_val, nums[left], nums[right]] 
                    break

            i += 1

        return list(res.values())

if True:
    def threeSum(nums) -> List[List[int]]:
        i = 0
        nums = sorted(nums)
        l = len(nums)

        if l <= 2:
            return []
        
        res = {}

        #Loop iterates over nums, -2 to ensure there are at least two more elements after the current nums[i]
        while i <= l - 2:
            start_val = nums[i]     #the current value at index[i]
            left = i + 1            #left is the index after i
            right = l - 1           #right is the last index of nums

            #This while loop checks if the sum of start_val, nums[left] and nums[right] is zero
            #If the sum is zero the triplet is added to res using a string key for uniqueness

            #After a valid triplet, left is incremented and moved past duplicates
            #If sum is less than zero, left is incremented to increase the sum
            #If sum is greater than zero, right is decremented to decrease the sum
            while left < right:
                total = nums[left] + nums[right]
                if start_val + total == 0:
                    res[f"{start_val}_{nums[left]}_{nums[right]}"] = [start_val, nums[left], nums[right]] 
                    left += 1
                    while left < l and nums[left] == nums[left-1]:
                        left += 1
                elif start_val + total < 0:
                    left += 1
                elif start_val + total > 0:
                    right -= 1

                if left >= l:
                    break

            i += 1

        return list(res.values())

print(f"{threeSum(caseNums_1)}")
print(f"{threeSum(caseNums_2)}")
print(f"{threeSum(caseNums_3)}")
print(f"{threeSum(caseNums_4)}")