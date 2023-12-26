#Power Of Two
#https://leetcode.com/problems/power-of-two/description/

caseNum_1 = 1
caseNum_2 = 16
caseNum_3 = 3

if True:
    def isPowerOfTwo(num) -> bool:
        result = 1
        while num > result:
            result *= 2
        
        return result == num
    
print(f"{isPowerOfTwo(caseNum_1)}")
print(f"{isPowerOfTwo(caseNum_2)}")
print(f"{isPowerOfTwo(caseNum_3)}")