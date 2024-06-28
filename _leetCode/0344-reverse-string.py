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

if False:
    def reverseString(s):
        halfway = math.floor(len(s)/2)
        for i in range(halfway):
            mirrorPoint = len(s) - 1 - i
            s[i], s[mirrorPoint] = s[mirrorPoint], s[i]

        return s

if False:
    def reverseString(s):
        left, right = 0, len(s)-1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        
        return s
    
if False:
    def reverseString(s):
        return s.reverse()

if True:
    def reverseString(s):
        #Slice assignment is needed as otherwise row would refer to 
        #a new list object and not modify the current?
        s[:] = s[::-1]
        return s
    
print(f"{reverseString(caseList_1)}")
print(f"{reverseString(caseList_2)}")