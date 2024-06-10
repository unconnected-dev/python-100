#Complement Of Base 10 Integer
#https://leetcode.com/problems/complement-of-base-10-integer/description/

caseN_1 = 5
caseN_2 = 7
caseN_3 = 10

if True:
    def bitwiseComplement(n):
        b = bin(n)[2:]
        
        s = ""
        for c in b:
            if c == "1":
                s += "0"
            else:
                s += "1"
        
        return int(s, 2)
    
print(f"{bitwiseComplement(caseN_1)}")
print(f"{bitwiseComplement(caseN_2)}")
print(f"{bitwiseComplement(caseN_3)}")