#Find The Index Of The First Occurence In A String
#https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

caseHaystack_1 = "sadbutsad"
caseNeedle_1 = "sad"

caseHaystack_2 = "leetcode"
caseNeedle_2 = "leeto"

caseHaystack_3 = "a"
caseNeedle_3 = "a"

if True:
    def strStr(haystack, needle):
        return haystack.index(needle) if needle in haystack else -1
    
print(f"{strStr(caseHaystack_1, caseNeedle_1)}")
print(f"{strStr(caseHaystack_2, caseNeedle_2)}")
print(f"{strStr(caseHaystack_3, caseNeedle_3)}")