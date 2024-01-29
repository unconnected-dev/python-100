#Smallest Even Multiple
#https://leetcode.com/problems/smallest-even-multiple/description/

caseNum_1 =5
caseNum_2 = 6

if True:
    def smallestEvenMultiple(num):
        if num % 2 != 0:
            return num * 2
        else:
            return num

print(f"{smallestEvenMultiple(caseNum_1)}")
print(f"{smallestEvenMultiple(caseNum_2)}")