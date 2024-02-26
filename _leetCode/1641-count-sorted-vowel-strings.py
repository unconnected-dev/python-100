#Count Sorted Vowel Strings
#https://leetcode.com/problems/count-sorted-vowel-strings/description/
import math

caseN_1 = 1
caseN_2 = 2
caseN_3 = 33

if False:
    def countVowelStrings(n):
        return (n + 4) * (n + 3) * (n + 2) * (n + 1) // 24

if True:
    def countVowelStrings(n):
        return math.comb(n + 4, 4)

print(f"{countVowelStrings(caseN_1)}")
print(f"{countVowelStrings(caseN_2)}")
print(f"{countVowelStrings(caseN_3)}")