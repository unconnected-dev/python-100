#Neither Mimimum Nor Maximum
#https://leetcode.com/problems/neither-minimum-nor-maximum/description/

caseNums_1 = [3,2,1,4]
caseNums_2 = [1,2]
caseNums_3 = [2,1,3]

if False:
    def findNonMinOrMax(nums):
        max_ = max(nums)
        min_ = min(nums)

        for n in nums:
            if n != max_ and n != min_:
                return n
        
        return -1

if True:
    def findNonMinOrMax(nums):
        if len(nums) < 3:
            return -1
        
        nums_slice = nums[:3]
        max_ = max(nums_slice)
        min_ = min(nums_slice)

        for n in nums_slice:
            if n != max_ and n != min_:
                return n

print(f"{findNonMinOrMax(caseNums_1)}")
print(f"{findNonMinOrMax(caseNums_2)}")
print(f"{findNonMinOrMax(caseNums_3)}")