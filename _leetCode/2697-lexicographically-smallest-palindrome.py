#Lexicographically Smallest Palindrome
#https://leetcode.com/problems/lexicographically-smallest-palindrome/description/

caseS_1 = "egcfe"
caseS_2 = "abcd"
caseS_3 = "seven"

if True:
    def makeSmallestPalindrome(s):
        left, right = 0, len(s) -1
        res = ""
        while left < len(s):
            if s[left] != s[right]:
                res += s[left] if s[left] < s[right] else s[right]
            else:
                res += s[left]

            left+=1
            right-=1 

        return res

print(f"{makeSmallestPalindrome(caseS_1)}")
print(f"{makeSmallestPalindrome(caseS_2)}")
print(f"{makeSmallestPalindrome(caseS_3)}")