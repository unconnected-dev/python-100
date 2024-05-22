#Replace All Digits With Characters
#https://leetcode.com/problems/replace-all-digits-with-characters/description/

caseS_1 = "a1c1e1"
caseS_2 = "a1b2c3d4e"

if True:
    def replaceDigits(s):

        def shift(c, n):
            return chr(ord(c) + int(n))
        
        res = ""
        for i in range(len(s)):
            res += shift(s[i-1], s[i]) if i%2 else s[i]
            
        return res

print(f"{replaceDigits(caseS_1)}")
print(f"{replaceDigits(caseS_2)}")