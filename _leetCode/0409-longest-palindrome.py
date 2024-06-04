#Longest Palindrome
#https://leetcode.com/problems/longest-palindrome/description/

import collections


caseS_1 = "abccccdd"
caseS_2 = "a"
caseS_3 = "bb"

if False:
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

if False:
    def longestPalindrome(s):
        my_set = set()
        for c in s:
            if c not in my_set:
                my_set.add(c)
            else:
                my_set.remove(c)
        
        if len(my_set) != 0:
            return len(s) - len(my_set) + 1
        else:
            return len(s)

if True:
    def longestPalindrome(s):
        res = 0
        count = collections.Counter(s)
        
        for v in count.values():
            res += v if v%2 == 0 else v -1
        
        one_odd = any(v%2==1 for v in count.values())
        
        return res + one_odd
        
print(f"{longestPalindrome(caseS_1)}")
print(f"{longestPalindrome(caseS_2)}")
print(f"{longestPalindrome(caseS_3)}")