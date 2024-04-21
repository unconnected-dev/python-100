#Koko Eating Bananas
#https://leetcode.com/problems/koko-eating-bananas/description/
import math

casePiles_1 = [3,6,7,11]
caseH_1 = 8

casePiles_2 = [30,11,23,4,20]
caseH_2 = 5

casePiles_3 = [30,11,23,4,20]
caseH_3 = 6

if True:
    def minEatingSpeed(piles, h):
        left, right = 1, max(piles)
        res = right
        
        while left <= right:
            mid = (left + right)//2
            hours = 0
            for p in piles:
                hours += math.ceil(p/mid)
            
            if hours <= h and mid < res:
                res = mid
                right = mid - 1
            else:
                left = mid + 1
                
        return res
    
print(f"{minEatingSpeed(casePiles_1, caseH_1)}")
print(f"{minEatingSpeed(casePiles_2, caseH_2)}")
print(f"{minEatingSpeed(casePiles_3, caseH_3)}")