#Three Divisors
#https://leetcode.com/problems/three-divisors/description/

caseN_1 = 2
caseN_2 = 4

if False:
    def isThree(n) -> bool:
        res = []
        for i in range(1, n + 1):
            if n % i == 0:
                res.append(i)
        
        return len(res) == 3

#Thought this would be faster due to being up to half n in range
if False:
    def isThree(n) -> bool:
        res = [1, n]
        for i in range(2, (n//2) + 1):
            if n%i == 0:
                res.append(i)

        return len(res) == 3

#If n was into higher ranges, this would break the loop quick
if True:
    def isThree(n) -> bool:
        res = [1, n]
        for i in range(2, (n//2) + 1):
            if n%i == 0:
                res.append(i)

                if len(res) > 3:
                    return False

        return len(res) == 3

print(f"{isThree(caseN_1)}")
print(f"{isThree(caseN_2)}")