#Keep Multiplying Found Values By Two
#https://leetcode.com/problems/keep-multiplying-found-values-by-two/description/

caseNums_1 = [5,3,6,1,12]
caseOriginal_1 = 3

caseNums_2 = [2,7,9]
caseOriginal_2 = 4


if False:
    def findFinalValue(nums, original):
        mySet = set(nums)

        while original in mySet:
            original = original * 2

        return original

if True:
    def findFinalValue(nums, original):
        my_set = set(nums)

        while original in my_set:
            my_set.remove(original)
            original *= 2
        
        return original

print(f"{findFinalValue(caseNums_1, caseOriginal_1)}")
print(f"{findFinalValue(caseNums_2, caseOriginal_2)}")