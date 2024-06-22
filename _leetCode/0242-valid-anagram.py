#Valid Anagram
#https://leetcode.com/problems/valid-anagram/description/
from collections import Counter


caseS_1 = "anagram"
caseT_1 = "nagaram"

caseS_2 = "rat"
caseT_2 = "car"

if False:
    def isAnagram(s, t) -> bool:

        if(len(s) != len(t)):
            return False
        
        s_sort = list(s.replace(" ", ""))
        t_sort = list(t.replace(" ", ""))
        s_sort.sort()
        t_sort.sort()

        return s_sort == t_sort 

if False:
    def isAnagram(s, t) -> bool:
        
        if(len(s) != len(t)):
            return False
        
        s_sort = sorted(s)
        t_sort = sorted(t)

        return s_sort == t_sort

if False:
    def isAnagram(s, t) -> bool:

        if(len(s) != len(t)):
            return False
        
        s_count = Counter(s)
        t_count = Counter(t)

        return s_count == t_count

if False:
    def isAnagram(s, t) -> bool:
        my_hash = {}
        for c in s:
            my_hash[c] = my_hash.get(c, 0) + 1
        
        my_other_hash = {}
        for c in t:
            my_other_hash[c] = my_other_hash.get(c, 0) + 1

        return my_hash == my_other_hash

if True:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)

print(f"{isAnagram(caseS_1, caseT_1)}")
print(f"{isAnagram(caseS_2, caseT_2)}")