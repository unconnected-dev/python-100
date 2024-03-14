#Perfect Number
#https://leetcode.com/problems/perfect-number/description/

import math

caseNum_1 = 28
caseNum_2 = 7

if False:
    def perfectNumber(num) -> bool:
        total = 0
        for i in range(1, math.floor(num/2) + 1):
            if num % i == 0:
                total += i

        return num == total

if True:
    def perfectNumber(num) -> bool:
        total = 0
        total += sum([n for n in range(1, math.floor(num/2) + 1) if num % n == 0])
        return total == num

print(f"{perfectNumber(caseNum_1)}")
print(f"{perfectNumber(caseNum_2)}")