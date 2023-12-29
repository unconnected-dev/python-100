#Number Of Good Pairs
#https://leetcode.com/problems/number-of-good-pairs/description/

caseNums_1 = [1,2,3,1,1,3]
caseNums_2 = [1,1,1,1]
caseNums_3 = [1,2,3]

if True:
    def numberOfGoodPairs(nums):
        goodPairs = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    goodPairs += 1

        return goodPairs

print(f"{numberOfGoodPairs(caseNums_1)}")
print(f"{numberOfGoodPairs(caseNums_2)}")
print(f"{numberOfGoodPairs(caseNums_3)}")