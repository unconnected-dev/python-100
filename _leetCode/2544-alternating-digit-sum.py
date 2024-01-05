#Alternating Digit Sum
#https://leetcode.com/problems/alternating-digit-sum/description/

caseNum_1 = 521
caseNum_2 = 111
caseNum_3 = 886996

if False:
    def alternatingDigitSum(n):
        total = 0
        nList = list(str(n))

        for i in range(0, len(nList), 2):
            total += int(nList[i])
        
        for i in range(1, len(nList), 2):
            total -= int(nList[i])
        
        return total

if True:
    def alternatingDigitSum(n):
        total = 0
        nList = list(str(n))
        e = 1

        for i in range(len(nList)):
            total += int(nList[i]) * e
            e *= -1
        
        return total


print(f"{alternatingDigitSum(caseNum_1)}")
print(f"{alternatingDigitSum(caseNum_2)}")
print(f"{alternatingDigitSum(caseNum_3)}")