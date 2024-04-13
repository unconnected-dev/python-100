#Binary Search
#https://leetcode.com/problems/binary-search/description/
import math

caseNums_1 = [-1,0,3,5,9,12]
caseTarget_1 = 9

caseNums_2 = [-1,0,3,5,9,12]
caseTarget_2 = 2

caseNums_3 = [5]
caseTarget_3 = 5

caseNums_4 = [2,5]
caseTarget_4 = 5

if True:
    def search(nums, target):
        l = len(nums) - 1
        i = math.floor(l/2)

        while l > 1:
            print(nums)
            print(i)
            if nums[i] == target:
                return i
            else:
                l = math.ceil(l/2)
                
                if nums[i] > target:
                    i -= l
                else:
                    i += l
        
        if nums[i] == target:
            return i
        
        return -1

print(f"{search(caseNums_1, caseTarget_1)}")
print(f"{search(caseNums_2, caseTarget_2)}")
print(f"{search(caseNums_3, caseTarget_3)}")
print(f"{search(caseNums_4, caseTarget_4)}")