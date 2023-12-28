#Intersection Of Two Arrays II
#https://leetcode.com/problems/intersection-of-two-arrays-ii/description/

caseNums1_1 = [1,2,2,1]
caseNums2_1 = [2,2]

caseNums1_2 = [4,9,5]
caseNums2_2 = [9,4,9,8,4]

if True:
    def intersectionOfTwoArraysII(nums1, nums2):
        countDict = dict()
        result = []

        for number in nums1:
            if number in countDict:
                countDict[number] += 1
            else:
                countDict[number] = 1
        
        for number in nums2:
            if number in countDict and countDict[number] > 0:
                result.append(number)
                countDict[number] -= 1

                if countDict[number] == 0:
                    countDict.pop(number)

        return result

print(f"{intersectionOfTwoArraysII(caseNums1_1, caseNums2_1)}")
print(f"{intersectionOfTwoArraysII(caseNums1_2, caseNums2_2)}")