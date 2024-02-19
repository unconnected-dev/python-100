#Sort Array By Parity
#https://leetcode.com/problems/sort-array-by-parity/description/

caseNums_1 = [3,1,2,4]
caseNums_2 = [0]

if False:
    def sortArrayByParity(nums):
        evens = []
        odds = []

        for n in nums:
            if n % 2== 0:
                evens.append(n)
            else:
                odds.append(n)
        
        evens += odds
        return evens

if True:
    def sortArrayByParity(nums):
        even_index = 0

        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i], nums[even_index] = nums[even_index], nums[i]
                even_index += 1

        return nums

print(f"{sortArrayByParity(caseNums_1)}")
print(f"{sortArrayByParity(caseNums_2)}")