#Longest Continuous Increasing Subsequence
#https://leetcode.com/problems/longest-continuous-increasing-subsequence/description/

caseNums_1 = [1,3,5,4,7]
caseNums_2 = [2,2,2,2,2]
caseNums_3 = [1,3,5,7]

if False:
    def findLengthOfLCIS(nums):
        res = [nums[0]]

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] > nums[j-1]:
                    if len(res) < len(nums[i:j+1]):
                        res = nums[i:j+1]
                else:
                    break

        return len(res)

if True:
    def findLengthOfLCIS(nums):
        res = 1

        for i in range(len(nums)):
            temp = 1
            for j in range(i+1, len(nums)):
                if nums[j] > nums[j-1]:
                    temp += 1
                else:
                    break
        
            if temp > res:
                res = temp

        return res
    
print(f"{findLengthOfLCIS(caseNums_1)}")
print(f"{findLengthOfLCIS(caseNums_2)}")
print(f"{findLengthOfLCIS(caseNums_3)}")