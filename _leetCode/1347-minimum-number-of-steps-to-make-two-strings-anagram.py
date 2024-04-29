#Minimum Number Of Steps To Make Two Strings Anagram
#https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/description/
from collections import Counter

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

if False:
    def minSteps(s, t):
        count = {}
        
        for c in s:
            count[c] = count.get(c, 0) + 1
        
        for c in t:
            if c in count and count.get(c) > 0:
                count[c] = count.get(c, 0) - 1    
        
        return sum(count.values())

if True:
    def minSteps(s, t):
        count_s = Counter(s)
        count_t = Counter(t)
        
        return sum((count_s - count_t).values())
        
print(f"{minSteps(caseS_1, caseT_1)}")
print(f"{minSteps(caseS_2, caseT_2)}")
print(f"{minSteps(caseS_3, caseT_3)}")