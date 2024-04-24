#N-th Tribonacci Number
#https://leetcode.com/problems/n-th-tribonacci-number/description/

caseN_1 = 4
caseN_2 = 25

if True:
    def tribonacci(n):
        
        a, b, c = 0, 1, 1
        
        for _ in range(n):
            a, b, c = b, c, a + b + c

        return a

print(f"{tribonacci(caseN_1)}")
print(f"{tribonacci(caseN_2)}")