#Number Of Changing Keys
#https://leetcode.com/problems/number-of-changing-keys/description/

caseS_1 = "aAbBcC"
caseS_2 = "AaAaAaaA"

if True:
    def countKeyChanges(s):
        res = 0
        for i in range(len(s)-1):
            if s[i].lower() != s[i+1].lower():
                res += 1

        return res
    
print(f"{countKeyChanges(caseS_1)}")
print(f"{countKeyChanges(caseS_2)}")