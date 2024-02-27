#Three Consecutive Odds
#https://leetcode.com/problems/three-consecutive-odds/description/

caseArr_1 = [2,6,4,1]
caseArr_2 = [1,2,34,3,4,5,7,23,12]

if True:
    def threeConsecutiveOdds(arr):
        for i in range(len(arr)):
            if arr[i] % 2 != 0:
                if i+2 < len(arr) and arr[i+1] % 2 != 0 and arr[i+2] % 2 != 0:
                    return True
        
        return False

print(f"{threeConsecutiveOdds(caseArr_1)}")
print(f"{threeConsecutiveOdds(caseArr_2)}")