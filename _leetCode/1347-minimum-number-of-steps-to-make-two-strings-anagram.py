#Minimum Number Of Steps To Make Two Strings Anagram
#https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/description/

caseS_1 = "bab"
caseT_1 = "aba"

caseS_2 = "leetcode"
caseT_2 = "practice"

caseS_3 = "anagram"
caseT_3 = "mangaar"

if True:
    def minSteps(s, t):
        for c in s:
            t = t.replace(c, '', 1)
        
        return len(t)

print(f"{minSteps(caseS_1, caseT_1)}")
print(f"{minSteps(caseS_2, caseT_2)}")
print(f"{minSteps(caseS_3, caseT_3)}")