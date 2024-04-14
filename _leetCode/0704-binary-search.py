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
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1

print(f"{search(caseNums_1, caseTarget_1)}")
print(f"{search(caseNums_2, caseTarget_2)}")
print(f"{search(caseNums_3, caseTarget_3)}")
print(f"{search(caseNums_4, caseTarget_4)}")