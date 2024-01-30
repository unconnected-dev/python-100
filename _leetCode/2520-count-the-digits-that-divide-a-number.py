#Count The Digits That Divide A Number
#https://leetcode.com/problems/count-the-digits-that-divide-a-number/description/

caseNum_1 = 7
caseNum_2 = 121
caseNum_3 = 1248

if False:
    def countDigits(num):
        c = 0
        ns = str(num)

        for i in range(len(ns)):
            if num % int(ns[i]) == 0:
                c += 1

        return c

if True:
    def countDigits(num):
        c = 0
        ns = str(num)

        for digit in ns:
            if num % int(digit) == 0:
                c += 1

        return c


print(f"{countDigits(caseNum_1)}")
print(f"{countDigits(caseNum_2)}")
print(f"{countDigits(caseNum_3)}")
