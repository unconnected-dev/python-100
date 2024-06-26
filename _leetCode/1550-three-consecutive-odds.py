#Three Consecutive Odds
#https://leetcode.com/problems/three-consecutive-odds/description/

from typing import List


caseArr_1 = [2,6,4,1]
caseArr_2 = [1,2,34,3,4,5,7,23,12]

if False:
    def threeConsecutiveOdds(arr):
        for i in range(len(arr)):
            if arr[i] % 2 != 0:
                if i+2 < len(arr) and arr[i+1] % 2 != 0 and arr[i+2] % 2 != 0:
                    return True
        
        return False

if False:
    def threeConsecutiveOdds(arr):
        for i in range(len(arr)-2):
            if arr[i] % 2 != 0 and arr[i+1] % 2 != 0 and arr[i+2] % 2 != 0:
                    return True
        return False

if True:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:

        def isOdd(num):
            return True if num%2!=0 else False
        
        for i in range(len(arr) - 2):
            if isOdd(arr[i]) and isOdd(arr[i+1]) and isOdd(arr[i+2]):
                return True
        
        return False

print(f"{threeConsecutiveOdds(caseArr_1)}")
print(f"{threeConsecutiveOdds(caseArr_2)}")