#Longest Substring Without Repeating Characters
#https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

caseS_1 = "abcabcbb"
caseS_2 = "bbbbb"
caseS_3 = "pwwkew"
caseS_4 = " "
caseS_5 = "dvdf"

if True:
    def lengthOfLongestSubstring(s: str) -> int:
        
        if len(s) == 0:
            return 0

        i, j = 0, 0
        my_set = set()
        res = 0

        while j < len(s):

            if s[j] not in my_set:
                my_set.add(s[j])
                j += 1
                res = max(res, j - i)
            else: 
                while s[i] != s[j]:
                    my_set.remove(s[i])
                    i += 1
                
                my_set.remove(s[i])
                i += 1

        return res
    
print(f"{lengthOfLongestSubstring(caseS_1)}")
print(f"{lengthOfLongestSubstring(caseS_2)}")
print(f"{lengthOfLongestSubstring(caseS_3)}")
print(f"{lengthOfLongestSubstring(caseS_4)}")
print(f"{lengthOfLongestSubstring(caseS_5)}")