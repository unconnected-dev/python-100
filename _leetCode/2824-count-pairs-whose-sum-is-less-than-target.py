#Count Pairs WHose Sum Is Less Than Target
#https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/description/

caseNums_1 = [-1,1,2,3,1]
caseTarget_1 = 2

caseNums_2 = [-6,2,5,-2,-7,-1,3]
caseTarget_2 = -2

if True:
    def countPairs(nums, target):
        c = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] < target:
                    c+=1

        return c

print(f"{countPairs(caseNums_1, caseTarget_1)}")
print(f"{countPairs(caseNums_2, caseTarget_2)}")