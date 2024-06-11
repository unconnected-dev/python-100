#Complement Of Base 10 Integer
#https://leetcode.com/problems/complement-of-base-10-integer/description/

caseN_1 = 5
caseN_2 = 7
caseN_3 = 10

if False:
    def bitwiseComplement(n):
        b = bin(n)[2:]
        
        s = ""
        for c in b:
            if c == "1":
                s += "0"
            else:
                s += "1"
        
        return int(s, 2)

if True:
    def bitwiseComplement(n):
        b = bin(n)[2:]
        return int(''.join(["1" if c == "0" else "0" for c in b]),2)
        
    
print(f"{bitwiseComplement(caseN_1)}")
print(f"{bitwiseComplement(caseN_2)}")
print(f"{bitwiseComplement(caseN_3)}")