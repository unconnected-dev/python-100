#Power Of Three
#https://leetcode.com/problems/power-of-three/description/

caseNum_1 = 27
caseNum_2 = 0
caseNum_3 = -1

if False:
    def powerOfThree(n) -> bool:
        if n < 1:
            return False
    
        while n > 1:
            if n % 3 != 0:
                return False
            
            n = n / 3

        return True

if False:
    def powerOfThree(n) -> bool:
        if n == 0:
            return False
    
        while n % 3 == 0:
            n = n // 3

        return n == 1

if True:
    def powerOfThree(n) -> bool:
        while n > 1:
            n /= 3
        
        return n == 1

print(f"{powerOfThree(caseNum_1)}")
print(f"{powerOfThree(caseNum_2)}")
print(f"{powerOfThree(caseNum_3)}")