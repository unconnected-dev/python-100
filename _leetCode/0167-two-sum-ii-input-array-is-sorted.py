#Two Sum II - Input Array Is Sorted
#https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

caseNumbers_1 = [2,7,11,15]
caseTarget_1 = 9

caseNumbers_2 = [2,3,4]
caseTarget_2 = 6

caseNumbers_3 = [-1,0]
caseTarget_3 = -1

if True:
    def twoSum(numbers, target):
        left = 0
        right = len(numbers) - 1

        while left < right:
            total = numbers[left] + numbers[right]
            if total == target:
                return [left+1, right+1]
            elif total < target:
                left += 1
            elif total > target:
                right -= 1

        return None

print(f"{twoSum(caseNumbers_1, caseTarget_1)}")
print(f"{twoSum(caseNumbers_2, caseTarget_2)}")
print(f"{twoSum(caseNumbers_3, caseTarget_3)}")