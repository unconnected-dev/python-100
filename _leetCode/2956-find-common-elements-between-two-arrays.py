#Find Common Elements Between Two Arrays
#https://leetcode.com/problems/find-common-elements-between-two-arrays/description/

caseNums1_1 = [4,3,2,3,1]
caseNums2_1 = [2,2,5,2,3,6]

caseNums1_2 = [3,4,2,3]
caseNums2_2 = [1,5]

if True:
    def findIntersectionValues(nums1, nums2):
        my_set_1 = set(nums1)
        my_set_2 = set(nums2)

        a = 0
        for i in range(len(nums1)):
            if nums1[i] in my_set_2:
                a += 1

        b = 0
        for i in range(len(nums2)):
            if nums2[i] in my_set_1:
                b += 1

        return [a,b]

print(f"{findIntersectionValues(caseNums1_1, caseNums2_1)}")
print(f"{findIntersectionValues(caseNums1_2, caseNums2_2)}")