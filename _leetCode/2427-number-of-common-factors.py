#Number Of Common Factors
#https://leetcode.com/problems/number-of-common-factors/description/

caseA_1 = 12
caseB_1 = 6

caseA_2 = 25
caseB_2 = 30

if False:
    def commonFactors(a, b):
        al = [n for n in range(1, a + 1) if a % n == 0]
        bl = [n for n in range(1, a + 1) if b % n == 0]
        
        return len([n for n in al if n in bl])

if False:
    def commonFactors(a, b):
        a_set = set([n for n in range(1, a + 1) if a % n == 0])
        bl = [n for n in range(1, a + 1) if b % n == 0 and n in a_set]
        return len(bl)

if True:
    def commonFactors(a, b):
        res = 0
        lowest_num = min(a, b)
        for i in range(1, lowest_num + 1):
            if a%i==0 and b%i==0:
                res += 1

        return res

print(f"{commonFactors(caseA_1, caseB_1)}")
print(f"{commonFactors(caseA_2, caseB_2)}")