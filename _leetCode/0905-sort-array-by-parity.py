#Sort Array By Parity
#https://leetcode.com/problems/sort-array-by-parity/description/

caseNums_1 = [3,1,2,4]
caseNums_2 = [0]

if True:
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
        

print(f"{sortArrayByParity(caseNums_1)}")
print(f"{sortArrayByParity(caseNums_2)}")
