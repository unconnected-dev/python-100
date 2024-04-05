#Sort Array By Parity
#https://leetcode.com/problems/sort-array-by-parity/description/

caseNums_1 = [3,1,2,4]
caseNums_2 = [0]
caseNums_3 = [0,1,2]
caseNums_4 = [0,2,1]

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

if False:
    def sortArrayByParity(nums):
        even_index = 0

        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i], nums[even_index] = nums[even_index], nums[i]
                even_index += 1

        return nums

if False:
    def sortArrayByParity(nums):
        evens, odds = [], []
        f = lambda n: n % 2 == 0
        for n in nums:
            evens.append(n) if f(n) else odds.append(n)
        
        return evens + odds

if True:
    def sortArrayByParity(nums):
        left = 0
        for _ in range(0, len(nums)):
            left = _
            if nums[_] % 2 != 0:
                break
        
        right = left
        for _ in range(right, len(nums)):
            if nums[left] % 2 != 0 and nums[_] % 2 == 0:
                nums[left], nums[_] = nums[_], nums[left]
                left += 1
        
        return nums
    
print(f"{sortArrayByParity(caseNums_1)}")
print(f"{sortArrayByParity(caseNums_2)}")
print(f"{sortArrayByParity(caseNums_3)}")
print(f"{sortArrayByParity(caseNums_4)}")