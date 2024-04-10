#Merge Similar Items
#https://leetcode.com/problems/merge-similar-items/description/

caseItems1_1 = [[1,1],[4,5],[3,8]]
caseItems2_1 = [[3,1],[1,5]]

caseItems1_2 = [[1,1],[3,2],[2,3]]
caseItems2_2 = [[2,1],[3,2],[1,3]]

caseItems1_3 = [[1,3],[2,2]]
caseItems2_3 = [[7,1],[2,2],[1,4]]

if False:
    def mergeSimilarItems(items1, items2):

        myDict = dict()
        for item in items1:
            if myDict.get(item[0]) is not None:
                myDict[item[0]] += item[1]
            else:
                myDict[item[0]] = item[1]

        for item in items2:
            if myDict.get(item[0]) is not None:
                myDict[item[0]] += item[1]
            else:
                myDict[item[0]] = item[1]

        sortedList = sorted(myDict.items())
        myList = []
        for value in sortedList:
             myList.append([value[0], value[1]])

        return myList

if False:
    def mergeSimilarItems(items1, items2):

        myDict = dict()
        for item in items1:
            myDict[item[0]] = myDict.get(item[0], 0) + item[1]

        for item in items2:
            myDict[item[0]] = myDict.get(item[0], 0) + item[1]

        sortedList = sorted(myDict.items())
        myList = []
        for value in sortedList:
             myList.append([value[0], value[1]])

        return myList

if True:
    def mergeSimilarItems(items1, items2):
        my_dict = {}
        for item in items1:
            my_dict[item[0]] = my_dict.get(item[0],0) + item[1]

        for item in items2:
            my_dict[item[0]] = my_dict.get(item[0],0) + item[1]

        sorted_list = sorted(my_dict.items())
        res = [0] * len(sorted_list)
        for i in range(len(sorted_list)):
            res[i] = [sorted_list[i][0],sorted_list[i][1]]

        return res
    
print(f"{mergeSimilarItems(caseItems1_1, caseItems2_1)}")
print(f"{mergeSimilarItems(caseItems1_2, caseItems2_2)}")
print(f"{mergeSimilarItems(caseItems1_3, caseItems2_3)}")