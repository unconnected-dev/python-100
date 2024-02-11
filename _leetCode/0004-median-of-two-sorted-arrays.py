#Median Of Two Sorted Arrays
#https://leetcode.com/problems/median-of-two-sorted-arrays/description/
import math

caseNums1_1 = [1,3]
caseNums2_1 = [2]

caseNums2_1 = [1,2]
caseNums2_2 = [3,4]

if True:
    def findMedianSortedArrays(nums1, nums2):
        nums3 = sorted(nums1 + nums2)
        length = len(nums3)

        if length % 2 != 0:
            return nums3[length // 2]
        else:
            return (nums3[length // 2] + nums3[length // 2 - 1]) / 2

print(f"{findMedianSortedArrays(caseNums1_1, caseNums2_1)}")
print(f"{findMedianSortedArrays(caseNums2_1, caseNums2_2)}")