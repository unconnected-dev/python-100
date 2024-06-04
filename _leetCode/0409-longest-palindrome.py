#Longest Palindrome
#https://leetcode.com/problems/longest-palindrome/description/

caseS_1 = "abccccdd"
caseS_2 = "a"

if True:
    def longestPalindrome(s):
        my_dict = {}

        res = 0
        for c in s:
            my_dict[c] = my_dict.get(c, 0) + 1

            if my_dict.get(c) == 2:
                res += 2
                my_dict[c] -= 2
        
        for k,v in my_dict.items():
            if v == 1:
                res += 1
                break

        return res
    
print(f"{longestPalindrome(caseS_1)}")
print(f"{longestPalindrome(caseS_2)}")