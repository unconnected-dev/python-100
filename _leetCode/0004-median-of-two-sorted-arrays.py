#Median Of Two Sorted Arrays
#https://leetcode.com/problems/median-of-two-sorted-arrays/description/

caseNums1_1 = [1,3]
caseNums2_1 = [2]

caseNums2_1 = [1,2]
caseNums2_2 = [3,4]

if False:
    def findMedianSortedArrays(nums1, nums2):
        nums3 = sorted(nums1 + nums2)
        length = len(nums3)

        if length % 2 != 0:
            return nums3[length // 2]
        else:
            return (nums3[length // 2] + nums3[length // 2 - 1]) / 2

if True:
    def findMedianSortedArrays(nums1, nums2):
        nums3 = []
        n1_l, n2_l = len(nums1), len(nums2)
        n1, n2 = 0, 0
        
        length = n1_l + n2_l

        for _ in range(length):
            if n2 >= n2_l or (n1 < n1_l and nums1[n1] <= nums2[n2]):
                nums3.append(nums1[n1])
                n1+=1
            else:
                nums3.append(nums2[n2])
                n2+=1

        if length % 2 != 0:
            return nums3[length // 2]
        else:
            return (nums3[length // 2] + nums3[length // 2 - 1]) / 2
            
print(f"{findMedianSortedArrays(caseNums1_1, caseNums2_1)}")
print(f"{findMedianSortedArrays(caseNums2_1, caseNums2_2)}")