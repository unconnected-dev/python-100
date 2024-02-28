#Check If All A's Appears Before All B's
#https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/description/

caseS_1 = "aaabbb"
caseS_2 = "abab"
caseS_3 = "bbb"

if False:
    def checkString(s):
        first_b = False
        for c in s:
            if c == "a" and first_b == True:
                return False
            
            if c == "b":
                first_b = True
        
        return True

if True:
    def checkString(s):
        return "ba" not in s

print(f"{checkString(caseS_1)}")
print(f"{checkString(caseS_2)}")
print(f"{checkString(caseS_3)}")