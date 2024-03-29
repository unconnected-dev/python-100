#Remove Palindromic Subsequences
#https://leetcode.com/problems/remove-palindromic-subsequences/description/

caseS_1 = "ababa"
caseS_2 = "abb"
caseS_3 = "baabb"
caseS_4 = "ababb"
caseS_5 = "bbaabaaa"

if True:
    def removePalindromeSub(s):
        return 1 if s == s[::-1] else 2

print(f"{removePalindromeSub(caseS_1)}")
print(f"{removePalindromeSub(caseS_2)}")
print(f"{removePalindromeSub(caseS_3)}")
print(f"{removePalindromeSub(caseS_4)}")
print(f"{removePalindromeSub(caseS_5)}")