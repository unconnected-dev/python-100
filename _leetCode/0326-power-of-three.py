#Power Of Three
#https://leetcode.com/problems/power-of-three/description/

caseNum_1 = 27
caseNum_2 = 0
caseNum_3 = -1

if True:
    def powerOfThree(num) -> bool:
        if num < 1:
            return False
    
        while num > 1:
            if num % 3 != 0:
                return False
            
            num = num / 3

        return True
    
print(f"{powerOfThree(caseNum_1)}")
print(f"{powerOfThree(caseNum_2)}")
print(f"{powerOfThree(caseNum_3)}")