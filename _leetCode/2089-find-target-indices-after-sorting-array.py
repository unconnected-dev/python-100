#Find Target Indices After Sorting Array
#https://leetcode.com/problems/find-target-indices-after-sorting-array/description/

caseNums_1 = [1,2,5,2,3]
caseTarget_1 = 2

caseNums_2 = [1,2,5,2,3]
caseTarget_2 = 3

caseNums_3 = [1,2,5,2,3]
caseTarget_3 = 5

if True:
    def targetIndices(nums, target):
        nums.sort()
        result = []

        for i in range(len(nums)):
            if nums[i] == target:
                result.append(i)

        return result

print(f"{targetIndices(caseNums_1, caseTarget_1)}")
print(f"{targetIndices(caseNums_2, caseTarget_2)}")
print(f"{targetIndices(caseNums_3, caseTarget_3)}")