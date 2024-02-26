#Sum Of Digits In Base K
#https://leetcode.com/problems/sum-of-digits-in-base-k/description/

caseN_1 = 34
caseK_1 = 6

caseN_2 = 10
caseK_2 = 10

if True:
    def sumBase(n, k):
        result = 0

        while n != 0:
            result += n%k
            n=n//k
            
        return result

print(f"{sumBase(caseN_1, caseK_1)}")
print(f"{sumBase(caseN_2, caseK_2)}")