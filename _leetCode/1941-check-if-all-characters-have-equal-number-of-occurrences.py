#Check If All Characters Have Equal Number Of Occurences
#https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/description/

caseString_1 = "abacbc"
caseString_2 = "aaabb"

if True:
    def areOccurrencesEqual(s):
        myDict = dict()

        for c in s:
            myDict[c] = myDict.get(c, 0) + 1

        n = myDict.get(s[0])
        for val in myDict.values():
            if n != val:
                return False
        
        return True

print(f"{areOccurrencesEqual(caseString_1)}")
print(f"{areOccurrencesEqual(caseString_2)}")