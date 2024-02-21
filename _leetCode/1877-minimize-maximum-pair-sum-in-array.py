#Minimize Maximum Pair Sum In Array
#https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/description/

caseNums_1 = [3,5,2,3]
caseNums_2 = [3,5,4,2,4,6]

if False:
    def minPairSum(nums):
        nums.sort()
        left = 0
        right = len(nums) - 1
        result_list = []

        while left < len(nums)//2:
            result_list.append(nums[left] + nums[right])
            left += 1
            right -= 1
        
        return max(result_list)

if True:
    def minPairSum(nums):
        nums.sort()
        left = 0
        right = len(nums) - 1
        result = float('-inf')

        while left < len(nums)//2:
            result = max((nums[left] + nums[right]), result)
            left += 1
            right -= 1
        
        return result

print(f"{minPairSum(caseNums_1)}")
print(f"{minPairSum(caseNums_2)}")