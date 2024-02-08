#Two Out Of Three
#https://leetcode.com/problems/two-out-of-three/description/

caseNums1_1 = [1,1,3,2]
caseNums2_1 = [2,3]
caseNums3_1 = [3]

caseNums1_2 = [3,1]
caseNums2_2 = [2,3]
caseNums3_2 = [1,2]

caseNums1_3 = [1,2,2]
caseNums2_3 = [4,3,3]
caseNums3_3 = [5]

if True:
    def twoOutOfThree(nums1, nums2, nums3):
        num1Set = set(nums1)
        num2Set = set(nums2)
        num3Set = set(nums3)

        combinedSet = set()

        for num in num1Set:
            if num in num2Set or num in num3Set:
                combinedSet.add(num)
        
        for num in num2Set:
            if num in num3Set:
                combinedSet.add(num)

        return list(combinedSet);

print(f"{twoOutOfThree(caseNums1_1, caseNums2_1, caseNums3_1)}")
print(f"{twoOutOfThree(caseNums1_2, caseNums2_2, caseNums3_2)}")
print(f"{twoOutOfThree(caseNums1_3, caseNums2_3, caseNums3_3)}")