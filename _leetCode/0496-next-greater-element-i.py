#Next Greater Element I
#https://leetcode.com/problems/next-greater-element-i/

from typing import List


caseNums1_1 = [4,1,2]
caseNums2_1 = [1,3,4,2]

caseNums1_2 = [2,4]
caseNums2_2 = [1,2,3,4]

if True:
    def nextGreaterElement(nums1: List[int], nums2: List[int]) -> List[int]:
        res = []

        for n in nums1:
            try:
                ind = nums2.index(n)
            except ValueError:
                ind = -1
            
            nextHigh = -1

            if ind >= 0:
                for i in range(ind, len(nums2)):
                    if nums2[i] > n:
                        nextHigh = nums2[i]
                        break                        

            res.append(nextHigh)

        return res
    
print(f"{nextGreaterElement(caseNums1_1, caseNums2_1)}")
print(f"{nextGreaterElement(caseNums1_2, caseNums2_2)}")