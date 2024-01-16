#Valid Anagram
#https://leetcode.com/problems/valid-anagram/description/

caseS_1 = "anagram"
caseT_1 = "nagaram"

caseS_2 = "rat"
caseT_2 = "car"

if True:
    def validAnagram(s, t) -> bool:

        if(len(s) != len(t)):
            return False
        
        s_sort = list(s.replace(" ", ""))
        t_sort = list(t.replace(" ", ""))
        s_sort.sort()
        t_sort.sort()

        return s_sort == t_sort 

print(f"{validAnagram(caseS_1, caseT_1)}")
print(f"{validAnagram(caseS_2, caseT_2)}")