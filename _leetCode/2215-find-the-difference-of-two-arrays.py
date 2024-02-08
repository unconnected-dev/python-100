#Find The Difference Of Two Arrays
#https://leetcode.com/problems/find-the-difference-of-two-arrays/description/

caseNums1_1 = [1,2,3]
caseNums2_1 = [2,4,6]

caseNums1_2 = [1,2,3,3]
caseNums2_2 = [1,1,2,2]

if True:
    def findDifference(nums1, nums2):
        mySet1 = set(nums1)
        mySet2 = set(nums2)

        numA = []
        numB = []

        for s1 in mySet1:
            if s1 not in mySet2:
                numA.append(s1)
            else:
                mySet2.remove(s1)

        for s2 in mySet2:
            if s2 not in mySet1:
                numB.append(s2)

        return [numA, numB]

print(f"{findDifference(caseNums1_1, caseNums2_1)}")
print(f"{findDifference(caseNums1_2, caseNums2_2)}")