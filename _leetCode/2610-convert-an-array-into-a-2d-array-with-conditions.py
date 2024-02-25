#Convert An Array Into A 2D Array With Conditions
#https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/description/

caseNums_1 = [1,3,4,1,2,3,1]
caseNums_2 = [2,1,1]

if True:
    def findMartix(nums):
        result = []
        num_set = set(nums)

        while len(nums) > 0:
            row = []
            for n in num_set:
                if n in nums:
                    row.append(n)
                    nums.remove(n)

            result.append(row)

        return result

print(f"{findMartix(caseNums_1)}")
print(f"{findMartix(caseNums_2)}")