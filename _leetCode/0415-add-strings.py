#Add Strings
#https://leetcode.com/problems/add-strings/description/

caseNum1_1 = "11"
caseNum2_1 = "123"

caseNum1_2 = "456"
caseNum2_2 = "77"

caseNum1_3 = "0"
caseNum2_3 = "0"

if False:
    def addStrings(num1, num2) -> str:
        
        def strToInt(num):
            numDict = {
                "0":0,
                "1":1,
                "2":2,
                "3":3,
                "4":4,
                "5":5,
                "6":6,
                "7":7,
                "8":8,
                "9":9,
            }

            n = 0
            for d in num:
                n = n * 10 + numDict[d]
            
            return n
        
        return str(strToInt(num1) + strToInt(num2))
    
if True:
    def addStrings(num1, num2) -> str:
        num1 = list(num1)
        num2 = list(num2)

        carry = 0
        res = ""

        while num1 or num2 or carry:
            if num1:
                carry += int(num1.pop())
            if num2:
                carry += int(num2.pop())
            
            res += str((carry % 10))
            carry //= 10

        return res[::-1]

print(f"{addStrings(caseNum1_1, caseNum2_1)}")
print(f"{addStrings(caseNum1_2, caseNum2_2)}")
print(f"{addStrings(caseNum1_3, caseNum2_3)}")
