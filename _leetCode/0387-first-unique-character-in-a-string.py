#First Unique Character In A String
#https://leetcode.com/problems/first-unique-character-in-a-string/description/
import collections

caseString_1 = "leetcode"
caseString_2 = "loveleetcode"
caseString_3 = "aabb"

if False:
    def firstUniqueCharacter(s):
        myDict = dict()

        for c in s:
            myDict[c] = myDict.get(c, 0) + 1

        for key, value in myDict.items():
            if value == 1:
                return s.index(key)
        
        return -1

if True:
    def firstUniqueCharacter(s):
        my_dict = collections.Counter(s)

        for key, value in my_dict.items():
            if value == 1:
                return s.index(key)
        
        return -1

print(f"{firstUniqueCharacter(caseString_1)}")
print(f"{firstUniqueCharacter(caseString_2)}")
print(f"{firstUniqueCharacter(caseString_3)}")