#Smallest Even Multiple
#https://leetcode.com/problems/smallest-even-multiple/description/

caseNum_1 =5
caseNum_2 = 6

if False:
    def smallestEvenMultiple(n):
        if n % 2 != 0:
            return n * 2
        else:
            return n

if True:
    def smallestEvenMultiple(n):
        return n * 2 if n % 2 != 0 else n

print(f"{smallestEvenMultiple(caseNum_1)}")
print(f"{smallestEvenMultiple(caseNum_2)}")