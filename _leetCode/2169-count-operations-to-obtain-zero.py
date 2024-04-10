#Count Operations To Obtain Zero
#https://leetcode.com/problems/count-operations-to-obtain-zero/description/

caseNum1_1 = 2
caseNum2_1 = 3

caseNum1_2 = 10
caseNum2_2 = 10

if False:
    def countOperations(num1, num2):
        c = 0

        while num1 != 0 and num2 != 0:
            if num1 > num2:
                num1 -= num2
            else:
                num2 -= num1
            
            c += 1
        
        return c

if True:
    def countOperations(num1, num2):
        c = 0
        while num1 and num2:
            if num1 > num2: num1 -= num2
            else: num2 -= num1
            c += 1

        return c
    
print(f"{countOperations(caseNum1_1, caseNum2_1)}")
print(f"{countOperations(caseNum1_2, caseNum2_2)}")