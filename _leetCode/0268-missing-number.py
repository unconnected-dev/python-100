#Missing Number
#https://leetcode.com/problems/missing-number/description/

caseNums_1 = [3,0,1]
caseNums_2 = [0,1]
caseNums_3 = [9,6,4,2,3,5,7,0,1]

if False:
    def missingNumber(nums):
        numsSet = set(nums)

        for i in range(len(nums) + 1):
            if i not in (numsSet):
                return i

if True:
    def missingNumber(nums):
        for i in range(len(nums) + 1):
            if i not in nums:
                return i        

print(f"{missingNumber(caseNums_1)}")
print(f"{missingNumber(caseNums_2)}")
print(f"{missingNumber(caseNums_3)}")