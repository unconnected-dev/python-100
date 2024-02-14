#Faulty Keyboard
#https://leetcode.com/problems/faulty-keyboard/description/

caseS_1 = "string"
caseS_2 = "poiinter"

if True:
    def finalString(s):
        rs = ""

        for c in s:
            if c != "i":
                rs += c
            else:
                rs = rs[::-1]
        
        return rs

print(f"{finalString(caseS_1)}")
print(f"{finalString(caseS_2)}")