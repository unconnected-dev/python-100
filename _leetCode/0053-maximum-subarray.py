#Maximum Subarray
#https://leetcode.com/problems/maximum-subarray/description/

caseNums_1 = [-2,1,-3,4,-1,2,1,-5,4]
caseNums_2 = [1]
caseNums_3 = [5,4,-1,7,8]

if True:
    def maximumSubarray(nums) -> int:
        max_total = nums[0]
        max_current = nums[0]

        for i in range(1, len(nums)):
            if nums[i] > max_current + nums[i]:
                max_current = nums[i]
            else:
                max_current = max_current + nums[i]
            
            if max_current > max_total:
                max_total = max_current
        
        return max_total

print(f"{maximumSubarray(caseNums_1)}")    
print(f"{maximumSubarray(caseNums_2)}")    
print(f"{maximumSubarray(caseNums_3)}")