#Minimum Number Of Steps To Make Two Strings Anagram
#https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/description/

caseS_1 = "bab"
caseT_1 = "aba"

caseS_2 = "leetcode"
caseT_2 = "practice"

caseS_3 = "anagram"
caseT_3 = "mangaar"

if False:
    def minSteps(s, t):
        for c in s:
            t = t.replace(c, '', 1)
        
        return len(t)

if True:
    def minSteps(s, t):
        count = {}
        
        for c in s:
            count[c] = count.get(c, 0) + 1
        
        for c in t:
            if c in count and count.get(c) > 0:
                count[c] = count.get(c, 0) - 1    
        
        return sum(count.values())
        
print(f"{minSteps(caseS_1, caseT_1)}")
print(f"{minSteps(caseS_2, caseT_2)}")
print(f"{minSteps(caseS_3, caseT_3)}")