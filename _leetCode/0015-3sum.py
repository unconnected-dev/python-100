#3Sum
#https://leetcode.com/problems/3sum/description/

caseNums_1 = [-1,0,1,2,-1,-4]
caseNums_2 = [0,1,1]
caseNums_3 = [0,0,0]
caseNums_4 = [-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]

if False:
    def threeSum(nums):
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
    def threeSum(nums):
        i = 0
        nums = sorted(nums)
        l = len(nums)

        if l <= 2:
            return []
        
        res = {}
        while i <= l - 2:
            start_val = nums[i]
            left = i + 1
            right = l - 1

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