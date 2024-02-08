#Check If All Characters Have Equal Number Of Occurences
#https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/description/
from collections import Counter

caseString_1 = "abacbc"
caseString_2 = "aaabb"

if False:
    def areOccurrencesEqual(s):
        myDict = dict()

        for c in s:
            myDict[c] = myDict.get(c, 0) + 1

        n = myDict.get(s[0])
        for val in myDict.values():
            if n != val:
                return False
        
        return True

if False:
    def areOccurrencesEqual(s):
        myDict = dict()

        for c in s:
            myDict[c] = myDict.get(c, 0) + 1
        
        mySet = set(myDict.values())

        return len(mySet) == 1

if True:
    def areOccurrencesEqual(s):
        returnList = []

        for c in s:
            returnList.append(s.count(c))
        
        return len(set(returnList)) == 1

if False:
    def areOccurrencesEqual(s):
        mySet = set(Counter(s).values())
        return len(mySet) == 1

print(f"{areOccurrencesEqual(caseString_1)}")
print(f"{areOccurrencesEqual(caseString_2)}")