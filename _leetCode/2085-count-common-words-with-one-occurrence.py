#Count Common Words With One Occurrence
#https://leetcode.com/problems/count-common-words-with-one-occurrence/description/
from collections import Counter

caseWords1_1 = ["leetcode","is","amazing","as","is"]
caseWords2_1 = ["amazing","leetcode","is"]

caseWords1_2 = ["b","bb","bbb"]
caseWords2_2 = ["a","aa","aaa"]

caseWords1_3 = ["a","ab"]
caseWords2_3 = ["a","a","a","ab"]

if True:
    def countWords(words1, words2):
        words1_count = Counter(words1)
        words2_count = Counter(words2)
        res = 0
        for key, val in words1_count.items():
            if val == 1 and words2_count.get(key, 0) == 1:
                res += 1
                
        return res
    
print(f"{countWords(caseWords1_1, caseWords2_1)}")
print(f"{countWords(caseWords1_2, caseWords2_2)}")
print(f"{countWords(caseWords1_3, caseWords2_3)}")