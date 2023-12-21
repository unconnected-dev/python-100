#Sort The People
#https://leetcode.com/problems/sort-the-people/description/

caseNames_1 = ["Mary","John","Emma"]
caseNames_2 = ["Alice","Bob","Bob"]

caseHeights_1 = [180,165,170]
caseHeights_2 = [155,185,150]

if True:
    def sortThePeople(names, heights):
        combiList = []
        for i in range(len(names)):
            combiList.append([names[i], heights[i]])
        
        combiList = sorted(combiList, key = lambda x: x[1], reverse = True)
        
        sortedList = []
        for person in combiList:
            sortedList.append(person[0])

        return sortedList
    
    print(f"{sortThePeople(caseNames_1, caseHeights_1)}")
    print(f"{sortThePeople(caseNames_2, caseHeights_2)}")