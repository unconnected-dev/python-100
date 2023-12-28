#Reverse String
#https://leetcode.com/problems/reverse-string/description/

import math

caseList_1 = ["h","e","l","l","o"]
caseList_2 = ["H","a","n","n","a","h"]

if False:
    def reverseString(s):
        for i in range(math.floor(len(s)/2)):
            c = s[i]
            s[i] = s[len(s) - 1 - i]
            s[len(s) - 1 - i] = c
        
        return s

if True:
    def reverseString(s):
        halfway = math.floor(len(s)/2)
        for i in range(halfway):
            mirrorPoint = len(s) - 1 - i
            s[i], s[mirrorPoint] = s[mirrorPoint], s[i]

        return s

print(f"{reverseString(caseList_1)}")
print(f"{reverseString(caseList_2)}")