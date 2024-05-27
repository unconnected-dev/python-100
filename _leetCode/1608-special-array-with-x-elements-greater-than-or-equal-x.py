#Special Array With X Elements Greater Than Or Equal X
#https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/description/

from typing import List


caseNums_1 = [3,5]
caseNums_2 = [0,0]
caseNums_3 = [0,4,3,0,4]

if True:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        l = len(nums)

        for n in range(l + 1):
            c = sum(1 for num in nums if num >= n)

            if c == n:
                return n

        return -1

print(f"{specialArray(caseNums_1)}")
print(f"{specialArray(caseNums_2)}")
print(f"{specialArray(caseNums_3)}")