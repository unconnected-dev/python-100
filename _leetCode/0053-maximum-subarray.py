#Maximum Subarray
#https://leetcode.com/problems/maximum-subarray/description/

caseNums_1 = [-2,1,-3,4,-1,2,1,-5,4]
caseNums_2 = [1]
caseNums_3 = [5,4,-1,7,8]

if True:
    def maximumSubarray(nums):
        max_total = nums[0]
        max_current = nums[0]

        for i in range(1, len(nums)):
            if nums[i] > max_current + nums[i]:
                max_current = nums[i]
            else:
                max_current = max_current + nums[i]
            
            if max_current > max_total:
                max_total = max_current
        
        print(f"Max total: {max_total}")
    
    maximumSubarray(caseNums_1)
    maximumSubarray(caseNums_2)
    maximumSubarray(caseNums_3)