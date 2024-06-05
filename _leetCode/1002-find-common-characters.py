#Find Common Characters
#https://leetcode.com/problems/find-common-characters/description/

import collections


caseWords_1 = ["bella","label","roller"]
caseWords_2 = ["cool","lock","cook"]

if True:
    def commonChars(words):
        counts = collections.Counter(words[0])
        for word in words:
            counts &= collections.Counter(word)
        
        return list(counts.elements())
    
print(f"{commonChars(caseWords_1)}")
print(f"{commonChars(caseWords_2)}")