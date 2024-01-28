#Find Greatest Common Divisor Of Array
#https://leetcode.com/problems/find-greatest-common-divisor-of-array/description/

caseNums_1 = [2,5,6,9,10]
caseNums_2 = [7,5,6,8,3]
caseNums_3 = [3,3]

if True:
    def findGCD(nums):
        min_ = min(nums)
        max_ = max(nums)
        d = 1

        for i in range(1, min_ + 1):
            if min_ % i == 0 and max_ % i == 0:
                d = i
        
        return d

print(f"{findGCD(caseNums_1)}")
print(f"{findGCD(caseNums_2)}")
print(f"{findGCD(caseNums_3)}")