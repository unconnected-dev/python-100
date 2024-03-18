#Power Of Four
#https://leetcode.com/problems/power-of-four/description/

caseN_1 = 16
caseN_2 = 5
caseN_3 = 1

if True:
    def isPowerOfFour(n):
        while n > 1:
            n /= 4

        return n == 1


print(f"{isPowerOfFour(caseN_1)}")
print(f"{isPowerOfFour(caseN_2)}")
print(f"{isPowerOfFour(caseN_3)}")