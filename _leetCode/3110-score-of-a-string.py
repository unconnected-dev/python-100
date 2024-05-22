#Score Of A String
#https://leetcode.com/problems/score-of-a-string/description/

caseS_1 = "hello"
caseS_2 = "zaz"

if False:
    def scoreOfString(s):
        total = 0
        for i in range(len(s)-1):
            c1 = s[i]
            c2 = s[i+1]
            total += abs(ord(c1) - ord(c2))
            
        return total

if False:
    def scoreOfString(s):
        total = 0
        for i in range(len(s)-1):
            total += abs(ord(s[i]) - ord(s[i+1]))
            
        return total

if True:
    def scoreOfString(s):
        return sum([abs(ord(c1) - ord(c2)) for c1, c2 in zip(s[:-1], s[1:])])  
    

print(f"{scoreOfString(caseS_1)}")
print(f"{scoreOfString(caseS_2)}")