#Permutation Difference Between Two Strings
#https://leetcode.com/problems/permutation-difference-between-two-strings/description/

caseS_1 = "abc"
caseT_1 = "bac"

caseS_2 = "abcde"
caseT_2 = "edbac"

if True:
    def findPermutationDifference(s, t):
        total = 0
        
        for i in range(len(s)):
            c = s[i]
            total += abs(i - t.index(c))
            
        return total
    
print(f"{findPermutationDifference(caseS_1, caseT_1)}")
print(f"{findPermutationDifference(caseS_2, caseT_2)}")