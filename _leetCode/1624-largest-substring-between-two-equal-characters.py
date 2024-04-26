#Largest Subtring Between Two Equal Characters
#https://leetcode.com/problems/largest-substring-between-two-equal-characters/description/

caseS_1 = "ss"
caseS_2 = "abca"
caseS_3 = "cbzxy"

if False:
    def maxLengthBetweenEqualCharacters(s):
        right = len(s)-1
        max_ = 0
        
        while right > 0:
            i = s.index(s[right])
            if i != right:
                max_ = max(max_, right-i)
                
            right -= 1

        return max_-1

if True:
    def maxLengthBetweenEqualCharacters(s):
        res = -1
        
        for c in set(s):
            res = max(res, s.rindex(c) - s.index(c)-1)
        
        return res

print(f"{maxLengthBetweenEqualCharacters(caseS_1)}")
print(f"{maxLengthBetweenEqualCharacters(caseS_2)}")
print(f"{maxLengthBetweenEqualCharacters(caseS_3)}")
