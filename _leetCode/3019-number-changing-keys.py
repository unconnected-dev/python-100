#Number Of Changing Keys
#https://leetcode.com/problems/number-of-changing-keys/description/

caseS_1 = "aAbBcC"
caseS_2 = "AaAaAaaA"

if False:
    def countKeyChanges(s):
        res = 0
        for i in range(len(s)-1):
            if s[i].lower() != s[i+1].lower():
                res += 1

        return res
    
if False:
    def countKeyChanges(s):
        return sum([1 if a.lower() != b.lower() else 0 for a, b in zip(s[:-1], s[1:])])

if False:
    def countKeyChanges(s):
        res = 0
        for i in range(len(s)-1):
            a = s[i]
            b = s[i+1]
            res += 1 if a.lower() != b.lower() else 0
        
        return res

if True:
    def countKeyChanges(s):
        s = s.lower()
        res = 0
        for i in range(len(s)-1):
            if s[i] != s[i+1]:
                res += 1
        
        return res
    
print(f"{countKeyChanges(caseS_1)}")
print(f"{countKeyChanges(caseS_2)}")