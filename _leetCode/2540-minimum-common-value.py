#Minimum Common Value
#https://leetcode.com/problems/minimum-common-value/description/

caseNums1_1 = [1,2,3]
caseNums2_1 = [2,4]

caseNums1_2 = [1,2,3,6]
caseNums2_2 = [2,3,4,5]

if False:
    def getCommon(nums1, nums2):
        lowest = float('inf')
        found = False
        for n in nums1:
            if n < lowest and n >= nums2[0] and n in nums2:
                lowest = n
                found = True
            elif found == True:
                break
            
        if lowest < float('inf'):
            return lowest
        else:
            return -1

if True:
    def getCommon(nums1, nums2):
        sets_combined = set(nums1) & set(nums2)
        return min(sets_combined) if len(sets_combined) > 0 else -1

print(f"{getCommon(caseNums1_1, caseNums2_1)}")
print(f"{getCommon(caseNums1_2, caseNums2_2)}")