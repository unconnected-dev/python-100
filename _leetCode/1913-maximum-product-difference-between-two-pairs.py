#Maximum Product Difference Between Two Pairs
#https://leetcode.com/problems/maximum-product-difference-between-two-pairs/description/

caseNums_1 = [5,6,2,7,4]
caseNums_2 = [4,2,5,9,7,4,8]

if True:
    def maxProductDifference(nums):
        nums_ = sorted(nums)
        a = nums_[-1]
        b = nums_[-2]
        c = nums_[0]
        d = nums_[1]

        return (a*b) - (c*d)
    
print(f"{maxProductDifference(caseNums_1)}")
print(f"{maxProductDifference(caseNums_2)}")