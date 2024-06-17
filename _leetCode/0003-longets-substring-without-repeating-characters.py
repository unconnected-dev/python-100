#Longest Substring Without Repeating Characters
#https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

caseS_1 = "abcabcbb"
caseS_2 = "bbbbb"
caseS_3 = "pwwkew"
caseS_4 = " "
caseS_5 = "dvdf"

if False:
    #Increment along with 2 pointers
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

if True:
    #Go through each character then create new substring as needed
    def lengthOfLongestSubstring(s: str) -> int:
        if len(s) == 0:
            return 0
        
        res, curr = 0, ""
        
        for c in s:
            if c not in curr:
                curr += c
            else:
                curr = curr[curr.index(c) + 1:] + c
            
            if len(curr) > res:
                res = len(curr)
        
        return res    

print(f"{lengthOfLongestSubstring(caseS_1)}")
print(f"{lengthOfLongestSubstring(caseS_2)}")
print(f"{lengthOfLongestSubstring(caseS_3)}")
print(f"{lengthOfLongestSubstring(caseS_4)}")
print(f"{lengthOfLongestSubstring(caseS_5)}")