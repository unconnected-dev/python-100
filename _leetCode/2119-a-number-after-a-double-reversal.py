#A Number After A Double Reversal
#https://leetcode.com/problems/a-number-after-a-double-reversal/description/

caseNum_1 = 526
caseNum_2 = 1800
caseNum_3 = 0

if False:
    def isSameAfterReversals(num):
        r1 = int(str(num)[::-1])
        r2 = int(str(r1)[::-1])

        return num == r2

if True:
    def isSameAfterReversals(num):
        return num == 0 or num % 10

print(f"{isSameAfterReversals(caseNum_1)}")
print(f"{isSameAfterReversals(caseNum_2)}")
print(f"{isSameAfterReversals(caseNum_3)}")