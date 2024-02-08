#Group The People Given The Group Size They Belong To
#https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/description/

caseGroupSizes_1 = [3,3,3,3,3,1,3]
caseGroupSizes_2 = [2,1,3,3,3,2]

if True:
    def groupThePeople(groupSizes):
        myDict = dict()
        returnList = []

        for index, size in enumerate(groupSizes):
            if size not in myDict:
                myDict[size] = []

            myDict[size].append(index)

            if len(myDict[size]) == size:
                returnList.append(myDict[size])
                del myDict[size]
        
        return returnList

print(f"{groupThePeople(caseGroupSizes_1)}")
print(f"{groupThePeople(caseGroupSizes_2)}")