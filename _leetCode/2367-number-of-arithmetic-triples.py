#Number Of Arithmetic Triplets
#https://leetcode.com/problems/number-of-arithmetic-triplets/description/

caseNums_1 = [0,1,4,6,7,10]
caseDiff_1 = 3

caseNums_2 = [4,5,6,7,8,9]
caseDiff_2 = 2

if True:
    def arithmeticTriplets(nums, diff):
        mySet = set(nums)
        total = 0

        for num in nums:
            if (num - diff) in mySet and (num + diff) in mySet:
                total += 1

        return total

print(f"{arithmeticTriplets(caseNums_1, caseDiff_1)}")
print(f"{arithmeticTriplets(caseNums_2, caseDiff_2)}")