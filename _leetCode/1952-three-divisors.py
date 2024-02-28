#Three Divisors
#https://leetcode.com/problems/three-divisors/description/

caseN_1 = 2
caseN_2 = 4

if True:
    def isThree(n):
        res = []
        for i in range(1, n + 1):
            if n % i == 0:
                res.append(i)
        
        return len(res) == 3

print(f"{isThree(caseN_1)}")
print(f"{isThree(caseN_2)}")