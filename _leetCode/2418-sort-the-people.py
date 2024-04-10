#Sort The People
#https://leetcode.com/problems/sort-the-people/description/

caseNames_1 = ["Mary","John","Emma"]
caseNames_2 = ["Alice","Bob","Bob"]

caseHeights_1 = [180,165,170]
caseHeights_2 = [155,185,150]

if False:
    def sortThePeople(names, heights):
        combiList = []
        for i in range(len(names)):
            combiList.append([names[i], heights[i]])
        
        combiList = sorted(combiList, key = lambda x: x[1], reverse = True)
        
        sortedList = []
        for person in combiList:
            sortedList.append(person[0])

        return sortedList

if True:
    def sortThePeople(names, heights):
        combined = [0] * len(names)
        for i in range(len(names)):
            combined[i] = [names[i], heights[i]]

        f = lambda a: a[1]
        combined = sorted(combined, key=f, reverse=True)

        res = [0] * len(names)
        for i in range(len(names)):
            res[i] = combined[i][0]
        
        return res

print(f"{sortThePeople(caseNames_1, caseHeights_1)}")
print(f"{sortThePeople(caseNames_2, caseHeights_2)}")