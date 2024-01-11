#Add Strings
#https://leetcode.com/problems/add-strings/description/

caseNum1_1 = "11"
caseNum2_1 = "123"

caseNum1_2 = "456"
caseNum2_2 = "77"

caseNum1_3 = "0"
caseNum2_3 = "0"

if True:
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
    
print(f"{addStrings(caseNum1_1, caseNum2_1)}")
print(f"{addStrings(caseNum1_2, caseNum2_2)}")
print(f"{addStrings(caseNum1_3, caseNum2_3)}")
