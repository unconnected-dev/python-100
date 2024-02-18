#Maximum Product Of Two Elements In An Array
#https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/description/

caseNums_1 = [3,4,5,2]
caseNums_2 = [1,5,4,5]
caseNums_3 = [3,7]

if True:
    def maxProduct(nums):
        a = float('-inf')
        b = float('-inf')

        for n in nums:
            if n > a:
                b = a
                a = n
            elif n > b and n <= a:
                b = n

        return (a-1) * (b-1)

print(f"{maxProduct(caseNums_1)}")
print(f"{maxProduct(caseNums_2)}")
print(f"{maxProduct(caseNums_3)}")