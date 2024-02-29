#Find The Index Of The First Occurence In A String
#https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

caseHaystack_1 = "sadbutsad"
caseNeedle_1 = "sad"

caseHaystack_2 = "leetcode"
caseNeedle_2 = "leeto"

caseHaystack_3 = "a"
caseNeedle_3 = "a"

if False:
    def strStr(haystack, needle):
        return haystack.index(needle) if needle in haystack else -1

if True:
    def strStr(haystack, needle):
        haystack_length = len(haystack)
        needle_length = len(needle)

        for i in range(haystack_length - needle_length + 1):
            if needle == haystack[i:i + needle_length]:
                return i
        
        return -1
    
print(f"{strStr(caseHaystack_1, caseNeedle_1)}")
print(f"{strStr(caseHaystack_2, caseNeedle_2)}")
print(f"{strStr(caseHaystack_3, caseNeedle_3)}")