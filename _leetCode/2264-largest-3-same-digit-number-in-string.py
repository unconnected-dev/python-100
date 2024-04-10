#Largest 3 Same Digit Number In String
#https://leetcode.com/problems/largest-3-same-digit-number-in-string/description/

caseNum_1 = "6777133339"
caseNum_2 = "2300019"
caseNum_3 = "42352338"

if False:
    def largestGoodInteger(num):
        l = ["999","888","777","666","555","444","333","222","111","000"]
        
        for n in l:
            if num.count(n) >= 1:
                return n
        
        return ""

if True:
    def largestGoodInteger(num):
        for n in range(9,-1,-1):
            if num.count(str(n)*3):
                return str(n)*3
        
        return ""

print(f"{largestGoodInteger(caseNum_1)}")
print(f"{largestGoodInteger(caseNum_2)}")
print(f"{largestGoodInteger(caseNum_3)}")