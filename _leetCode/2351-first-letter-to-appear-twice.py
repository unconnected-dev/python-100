#First Letter To Appear Twice
#https://leetcode.com/problems/first-letter-to-appear-twice/description/

caseString_1 = "abccbaacz"
caseString_2 = "abcdd"

if False:
    def repeatedCharacter(s):
        myDict = dict()

        for c in s:
            if c in myDict:
                return c
            else:
                myDict[c] = 1

if True:
    def repeatedCharacter(s):
        mySet = set()
        for c in s:
            if c in mySet:
                return c
            mySet.add(c)

print(f"{repeatedCharacter(caseString_1)}")
print(f"{repeatedCharacter(caseString_2)}")