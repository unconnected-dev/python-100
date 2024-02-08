#Increasing Decreasing String
#https://leetcode.com/problems/increasing-decreasing-string/description/
from collections import Counter

caseString_1 = "aaaabbbbcccc"
caseString_2 = "rat"

if False:
    def sortString(s):
        collectionDict = Counter(s).items()
        collectionList = sorted([c, n] for c, n in collectionDict)
        returnList = []
        
        while len(returnList) < len(s):
            for i in range(len(collectionList)):
                if collectionList[i][1]:
                    returnList.append(collectionList[i][0])
                    collectionList[i][1] -= 1
                    
            for i in range(len(collectionList) - 1, -1, -1):
                if collectionList[i][1]:
                    returnList.append(collectionList[i][0])
                    collectionList[i][1] -= 1
            
        return ''.join(returnList)

if True:
    def sortString(s):
        myDict = dict()

        sortedList = sorted(list(s))
        for c in sortedList:
            myDict[c] = myDict.get(c, 0) + 1

        returnList = []
        while len(returnList) < len(s):
            for key, val in myDict.items():
                if val > 0:
                    returnList.append(key)
                    myDict[key] = myDict.get(key, 0) - 1

            for key, val in reversed(myDict.items()):
                if val > 0:
                    returnList.append(key)
                    myDict[key] = myDict.get(key, 0) - 1

        return ''.join(returnList)

print(f"{sortString(caseString_1)}")
print(f"{sortString(caseString_2)}")