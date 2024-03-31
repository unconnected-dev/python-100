#Find Words Containing Character
#https://leetcode.com/problems/find-words-containing-character/description/
import re

caseWords_1 = ["leet","code"]
caseX_1 = "e"

caseWords_2 = ["abc","bcd","aaaa","cbc"]
caseX_2 = "a"

caseWords_3 = ["abc","bcd","aaaa","cbc"]
caseX_3 = "z"

if False:
    def findWordContaining(words, x):
        i = 0
        result = []
        for word in words:
            if x in word:
                result.append(i)
            i+=1

        return result

if False:
    def findWordContaining(words, x):
        result = []
        for i, word in enumerate(words):
            if x in word:
                result.append(i)
            
        return result

if True:
    def findWordContaining(words, x):
        res = []

        pattern = rf'{x}'
        for i, word in enumerate(words):
            match = re.search(pattern, word)
            if match:
                res.append(i)
        
        return res

print(f"{findWordContaining(caseWords_1, caseX_1)}")
print(f"{findWordContaining(caseWords_2, caseX_2)}")
print(f"{findWordContaining(caseWords_3, caseX_3)}")