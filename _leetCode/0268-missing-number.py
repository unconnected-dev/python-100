#Missing Number
#https://leetcode.com/problems/missing-number/description/

caseNums_1 = [3,0,1]
caseNums_2 = [0,1]
caseNums_3 = [9,6,4,2,3,5,7,0,1]


if True:
    def missingNumber(nums):
        nums_ = set(nums)

        for i in range(len(nums)):
            if i not in (nums_):
                print(f"{i}")
                break
    
    missingNumber(caseNums_1)
    missingNumber(caseNums_2)
    missingNumber(caseNums_3)