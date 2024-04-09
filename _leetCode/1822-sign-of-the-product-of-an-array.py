#Sign Of The Product Of An Array
#https://leetcode.com/problems/sign-of-the-product-of-an-array/

import math

caseNums_1 = [-1,-2,-3,-4,3,2,1]
caseNums_2 = [1,5,0,2,-3]
caseNums_3 = [-1,1,-1,1,-1]
caseNums_4 = [9,72,34,29,-49,-22,-77,-17,-66,-75,-44,-30,-24]

#Overflowerror
if False:
    def arraySign(nums):
        if 0 in nums:
            return 0
        else:
            t = nums[0]
            for i in range(1, len(nums)):
                t *= nums[i]
            
            return int(math.copysign(1, t))

if False:
    def arraySign(nums):
        res = 1
        for n in nums:
            if n == 0: return 0
            if n < 0: res *= -1

        return res

if True:
    def arraySign(nums):
        res = 0
        for n in nums:
            if n == 0: return 0
            if n < 0: res += 1
        
        return 1 if res%2 == 0 else -1

print(f"{arraySign(caseNums_1)}")
print(f"{arraySign(caseNums_2)}")
print(f"{arraySign(caseNums_3)}")
print(f"{arraySign(caseNums_4)}")
