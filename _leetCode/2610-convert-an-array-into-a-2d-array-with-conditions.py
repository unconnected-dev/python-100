#Convert An Array Into A 2D Array With Conditions
#https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/description/
import collections

caseNums_1 = [1,3,4,1,2,3,1]
caseNums_2 = [2,1,1]

if False:
    def findMatrix(nums):
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

if False:
    def findMatrix(nums):
        num_dict = {}
        for n in nums:
            num_dict[n] = num_dict.get(n, 0) + 1
        
        result = []
        while True:
            row = []

            for key, value in num_dict.items():
                if value > 0:
                    row.append(key)
                    num_dict[key] -= 1
            
            if len(row) > 0:
                result.append(row)
            else:
                break
        
        return result

if True:
    def findMatrix(nums):
        cl = collections.Counter(nums)
        res = []
        total = 0

        while total < len(nums):
            part = []
            for key, val in cl.items():
                if val > 0:
                    cl[key] = cl.get(key) - 1
                    part.append(key)
                    total += 1
            
            res.append(part)

        return res

print(f"{findMatrix(caseNums_1)}")
print(f"{findMatrix(caseNums_2)}")