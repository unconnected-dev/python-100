#Sign Of The Product Of An Array
#https://leetcode.com/problems/sign-of-the-product-of-an-array/

import math

caseNums_1 = [-1,-2,-3,-4,3,2,1]
caseNums_2 = [1,5,0,2,-3]
caseNums_3 = [-1,1,-1,1,-1]

if True:
    def arraySign(nums):
        if 0 in nums:
            return 0
        else:
            t = nums[0]
            for i in range(1, len(nums)):
                t *= nums[i]
            
            return math.copysign(1, t)

print(f"{arraySign(caseNums_1)}")
print(f"{arraySign(caseNums_2)}")
print(f"{arraySign(caseNums_3)}")
