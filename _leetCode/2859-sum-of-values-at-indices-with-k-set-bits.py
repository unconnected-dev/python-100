#Sum Of Values At Indices With K Set Bits
#https://leetcode.com/problems/sum-of-values-at-indices-with-k-set-bits/description/

caseNums_1 = [5,10,1,5,2]
caseK_1 = 1

caseNums_2 = [4,3,2,1]
caseK_2 = 2

if False:
    def sumIndicesWithKSetBits(nums, k):
        total = 0
        for i in range(len(nums)):
            if bin(i).count('1') == k:
                total += nums[i]

        return total

if True:
    def sumIndicesWithKSetBits(nums, k):
        total = 0
        for i in range(len(nums)):
            if bin(i)[2:].count('1') == k:
                total += nums[i]
        
        return total

print(f"{sumIndicesWithKSetBits(caseNums_1, caseK_1)}")
print(f"{sumIndicesWithKSetBits(caseNums_2, caseK_2)}")