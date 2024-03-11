#Valid Anagram
#https://leetcode.com/problems/valid-anagram/description/
from collections import Counter


caseS_1 = "anagram"
caseT_1 = "nagaram"

caseS_2 = "rat"
caseT_2 = "car"

if False:
    def validAnagram(s, t) -> bool:

        if(len(s) != len(t)):
            return False
        
        s_sort = list(s.replace(" ", ""))
        t_sort = list(t.replace(" ", ""))
        s_sort.sort()
        t_sort.sort()

        return s_sort == t_sort 

if False:
    def validAnagram(s, t) -> bool:
        
        if(len(s) != len(t)):
            return False
        
        s_sort = sorted(s)
        t_sort = sorted(t)

        return s_sort == t_sort

if True:
    def validAnagram(s, t) -> bool:

        if(len(s) != len(t)):
            return False
        
        s_count = Counter(s)
        t_count = Counter(t)

        return s_count == t_count

print(f"{validAnagram(caseS_1, caseT_1)}")
print(f"{validAnagram(caseS_2, caseT_2)}")