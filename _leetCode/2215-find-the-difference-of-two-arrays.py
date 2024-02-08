#Find The Difference Of Two Arrays
#https://leetcode.com/problems/find-the-difference-of-two-arrays/description/

caseNums1_1 = [1,2,3]
caseNums2_1 = [2,4,6]

caseNums1_2 = [1,2,3,3]
caseNums2_2 = [1,1,2,2]

if False:
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

if True:
    def findDifference(nums1, nums2):
        s1 = set(nums1)
        s2 = set(nums2)

        #If the `-` operator is used between two sets
        #It performs a set difference operation
        #returning a new set containing elements in the first set 
        #but not in the second set
        return[list(s1 - s2), list(s2 - s1)]

print(f"{findDifference(caseNums1_1, caseNums2_1)}")
print(f"{findDifference(caseNums1_2, caseNums2_2)}")