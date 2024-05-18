#Sqrt
#https://leetcode.com/problems/sqrtx/description/

caseX_1 = 4
caseX_2 = 8

if True:
    def mySqrt(x):
        res = x
        while res*res > x:
            res = (res+x//res)//2

        return res
    
print(f"{mySqrt(caseX_1)}")
print(f"{mySqrt(caseX_2)}")