#Merge Sorted Array
#https://leetcode.com/problems/merge-sorted-array/description/

caseNums1_1 = [1,2,3,0,0,0]
caseM_1 = 3
caseNums2_1 = [2,5,6]
caseN_1 = 3

caseNums1_2 = [1]
caseM_2 = 1
caseNums2_2 = []
caseN_2 = 0

caseNums1_3 = [0]
caseM_3 = 0
caseNums2_3 = [1]
caseN_3 = 1

if False:
    def merge(nums1, m, nums2, n):
        first = m - 1
        second = n - 1
        i = len(nums1) - 1

        while second >= 0:
            firstValue = nums1[first]
            secondValue = nums2[second]

            if firstValue > secondValue:
                nums1[i] = firstValue
                first -= 1
            else:
                nums1[i] = secondValue
                second -= 1
            
            i -= 1

        return nums1

if True:
    def merge(nums1, m, nums2, n):
        first = m - 1
        second = n - 1
        index_ = m + n - 1

        while second >= 0:
            if first >= 0 and nums1[first] > nums2[second]:
                nums1[index_] = nums1[first]
                first -= 1
            else:
                nums1[index_] = nums2[second]
                second -= 1
            
            index_ -= 1
        
        return nums1

print(f"{merge(caseNums1_1, caseM_1, caseNums2_1, caseN_1)}")
print(f"{merge(caseNums1_2, caseM_2, caseNums2_2, caseN_2)}")
print(f"{merge(caseNums1_3, caseM_3, caseNums2_3, caseN_3)}")