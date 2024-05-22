#Score Of A String
#https://leetcode.com/problems/score-of-a-string/description/

caseS_1 = "hello"
caseS_2 = "zaz"

if True:
    def scoreOfString(s):
        total = 0
        for i in range(len(s)-1):
            c1 = s[i]
            c2 = s[i+1]
            total += abs(ord(c1) - ord(c2))
            
        return total
    
print(f"{scoreOfString(caseS_1)}")
print(f"{scoreOfString(caseS_2)}")