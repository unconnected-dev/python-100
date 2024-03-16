#Longest Continuous Increasing Subsequence
#https://leetcode.com/problems/longest-continuous-increasing-subsequence/description/

caseNums_1 = [1,3,5,4,7]
caseNums_2 = [2,2,2,2,2]

if True:
    def findLenghtOfLCIS(nums):
        res = [nums[0]]

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] > nums[j-1]:
                    if len(res) < len(nums[i:j+1]):
                        res = nums[i:j+1]
                else:
                    break

        return len(res)

print(f"{findLenghtOfLCIS(caseNums_1)}")
print(f"{findLenghtOfLCIS(caseNums_2)}")