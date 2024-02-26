#Count Sorted Vowel Strings
#https://leetcode.com/problems/count-sorted-vowel-strings/description/

caseN_1 = 1
caseN_2 = 2
caseN_3 = 33

if True:
    def countVowelStrings(n):
        return (n + 4) * (n + 3) * (n + 2) * (n + 1) // 24

print(f"{countVowelStrings(caseN_1)}")
print(f"{countVowelStrings(caseN_2)}")
print(f"{countVowelStrings(caseN_3)}")