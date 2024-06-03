#Append Characters To String To Make Subsequence
#https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/description/

caseS_1 = "coaching"
caseT_1 = "coding"

caseS_2 = "abcde"
caseT_2 = "a"

caseS_3 = "z"
caseT_3 = "abcde"

caseS_4 = "lbg"
caseT_4 = "g"

if True:
    def appendCharacters(s, t):
        i, j = 0, 0

        while i < len(s) and j < len(t):
            if s[i]==t[j]:
                i += 1
                j += 1
            else:
                i += 1
        
        return len(t) - j

print(f"{appendCharacters(caseS_1, caseT_1)}")
print(f"{appendCharacters(caseS_2, caseT_2)}")
print(f"{appendCharacters(caseS_3, caseT_3)}")
print(f"{appendCharacters(caseS_4, caseT_4)}")