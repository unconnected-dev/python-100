#Power Of Four
#https://leetcode.com/problems/power-of-four/description/

caseN_1 = 16
caseN_2 = 5
caseN_3 = 1

if False:
    def isPowerOfFour(n) -> bool:
        while n > 1:
            n /= 4

        return n == 1

if False:
    def isPowerOfFour(n) -> bool:
        if n == 0:
            return False
        
        while n % 4 == 0:
            n = n // 4

        return n == 1

#Multiplying up
if True:
    def isPowerOfFour(n) -> bool:
        res = 1

        while n > res:
            res *= 4

        return res == n

print(f"{isPowerOfFour(caseN_1)}")
print(f"{isPowerOfFour(caseN_2)}")
print(f"{isPowerOfFour(caseN_3)}")