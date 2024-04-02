#Isomorphic Strings
#https://leetcode.com/problems/isomorphic-strings/description/

caseS_1 = "egg"
caseT_1 = "add"

caseS_2 = "foo"
caseT_2 = "bar"

caseS_3 = "paper"
caseT_3 = "title"

caseS_4 = "bbbaaaba"
caseT_4 = "aaabbbba"

caseS_5 = "abab"
caseT_5 = "baba"

if True:
    def isIsomorphic(s, t):
        s_t = {}
        t_s = {}
        for i in range(len(s)):
            if s_t.get(s[i], 0) == 0:
                s_t[s[i]] = t[i]
            elif s_t.get(s[i]) != t[i]:
                return False

            if t_s.get(t[i], 0) == 0:
                t_s[t[i]] = s[i]
            elif t_s.get(t[i]) != s[i]:
                return False        

        for key, val in s_t.items():
            if t_s.get(val, 0) != key:
                return False

        return True
    
print(f"{isIsomorphic(caseS_1, caseT_1)}")
print(f"{isIsomorphic(caseS_2, caseT_2)}")
print(f"{isIsomorphic(caseS_3, caseT_3)}")
print(f"{isIsomorphic(caseS_4, caseT_4)}")
print(f"{isIsomorphic(caseS_5, caseT_5)}")