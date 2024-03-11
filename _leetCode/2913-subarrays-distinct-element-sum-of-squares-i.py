#Subarrays Distinct Element Sum Of Squares I
#https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-i/description/

caseNums_1 = [1,2,1]
caseNums_2 = [1,1]

if True:
    def sumCounts(nums):
        res = []

        for i in range(len(nums)):
            for j in range(i, len(nums)+1):
                res.append(len(set(nums[i:j]))**2)
        
        return sum(res)

print(f"{sumCounts(caseNums_1)}")
print(f"{sumCounts(caseNums_2)}")