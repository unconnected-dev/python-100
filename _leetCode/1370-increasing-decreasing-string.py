#Increasing Decreasing String
#https://leetcode.com/problems/increasing-decreasing-string/description/
from collections import Counter

caseString_1 = "aaaabbbbcccc"
caseString_2 = "rat"

if True:
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

print(f"{sortString(caseString_1)}")
print(f"{sortString(caseString_2)}")