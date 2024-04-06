#Unique Number Of Occurrences
#https://leetcode.com/problems/unique-number-of-occurrences/description/

caseArr_1 = [1,2,2,1,1,3]
caseArr_2 = [1,2]
caseArr_3 = [-3,0,1,-3,1,1,1,-3,10,0]

if False:
    def uniqueOccurrences(arr):
        myDict = dict()

        for n in arr:
            myDict[n] = myDict.get(n, 0) + 1

        mySet = set()
        for key, value in myDict.items():
            mySet.add(value)

        return len(myDict) == len(mySet)

if True:
    def uniqueOccurrences(arr):
        my_set = set(arr)

        arr_count = []
        for n in my_set:
            arr_count.append(arr.count(n))

        arr_count_set = set(arr_count)

        return len(my_set) == len(arr_count_set)
    
print(f"{uniqueOccurrences(caseArr_1)}")
print(f"{uniqueOccurrences(caseArr_2)}")
print(f"{uniqueOccurrences(caseArr_3)}")