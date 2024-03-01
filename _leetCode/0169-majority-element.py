#Majority Element
#https://leetcode.com/problems/majority-element/description/
import math 

caseNums_1 = [3,2,3]
caseNums_2 = [2,2,1,1,1,2,2]
caseNums_3 = [4,5,4]

if True:
    def majorityElement(nums):
        l = len(nums)
        my_dict = {}

        for n in nums:
            my_dict[n] = my_dict.get(n, 0) + 1

            if my_dict.get(n) >= math.ceil(l/2):
                return n

print(f"{majorityElement(caseNums_1)}")
print(f"{majorityElement(caseNums_2)}")
print(f"{majorityElement(caseNums_3)}")