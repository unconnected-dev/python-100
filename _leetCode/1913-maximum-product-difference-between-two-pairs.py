#Maximum Product Difference Between Two Pairs
#https://leetcode.com/problems/maximum-product-difference-between-two-pairs/description/

caseNums_1 = [5,6,2,7,4]
caseNums_2 = [4,2,5,9,7,4,8]

if False:
    def maxProductDifference(nums):
        nums_ = sorted(nums)
        a = nums_[-1]
        b = nums_[-2]
        c = nums_[0]
        d = nums_[1]

        return (a*b) - (c*d)

if False:
    def maxProductDifference(nums):
        nums_ = sorted(nums)
        return (nums_[-1] * nums_[-2]) - (nums_[0] * nums_[1])

if True:
    def maxProductDifference(nums):
        a = float('-inf')
        b = float('-inf')
        c = float('inf')
        d = float('inf')

        for n in nums:
            if n >= a:
                b = a
                a = n
            elif b < n < a:
                b = n

            if n <= c:
                d = c
                c = n
            elif d > n > c:
                d = n

        return (a*b) - (c*d)



print(f"{maxProductDifference(caseNums_1)}")
print(f"{maxProductDifference(caseNums_2)}")