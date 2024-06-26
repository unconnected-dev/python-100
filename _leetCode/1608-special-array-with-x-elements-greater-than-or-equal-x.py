#Special Array With X Elements Greater Than Or Equal X
#https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/description/

from typing import List


caseNums_1 = [3,5]
caseNums_2 = [0,0]
caseNums_3 = [0,4,3,0,4]
caseNums_4 = [3,6,7,7,0]

if False:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        l = len(nums)

        for n in range(l + 1):
            c = sum(1 for num in nums if num >= n)

            if c == n:
                return n

        return -1

if True:
    def specialArray(nums):
        nums.sort()
        l = len(nums)

        def binary_search(num):
            left, right = 0, l - 1

            i = l
            while left <= right:
                mid = (left + right) // 2

                if nums[mid] >= num:
                    i = mid
                    right = mid - 1
                else:
                    left = mid + 1
            
            return l - i

        for n in range(1, l+1, 1):
            if n == binary_search(n):
                return n

        return -1

print(f"{specialArray(caseNums_1)}")
print(f"{specialArray(caseNums_2)}")
print(f"{specialArray(caseNums_3)}")
print(f"{specialArray(caseNums_4)}")