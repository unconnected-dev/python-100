#How Many Numbers Are Smaller Than The Current Number
#https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/description/

caseNums_1 = [8,1,2,2,3]
caseNums_2 = [6,5,4,8]
caseNums_3 = [7,7,7,7]

if True:
    def howManyNumbersAreSmallerThanTheCurrentNumber(nums):
        ind = []
        sortedNums = nums.copy()
        sortedNums.sort()
        
        for num in nums:
            ind.append(sortedNums.index(num))

        return ind

print(f"{howManyNumbersAreSmallerThanTheCurrentNumber(caseNums_1)}")
print(f"{howManyNumbersAreSmallerThanTheCurrentNumber(caseNums_2)}")
print(f"{howManyNumbersAreSmallerThanTheCurrentNumber(caseNums_3)}")