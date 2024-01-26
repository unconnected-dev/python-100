#Unique Number Of Occurrences
#https://leetcode.com/problems/unique-number-of-occurrences/description/

caseArr_1 = [1,2,2,1,1,3]
caseArr_2 = [1,2]
caseArr_3 = [-3,0,1,-3,1,1,1,-3,10,0]

if True:
    def uniqueOccurrences(arr):
        myDict = dict()

        for n in arr:
            myDict[n] = myDict.get(n, 0) + 1

        mySet = set()
        for key, value in myDict.items():
            mySet.add(value)

        return len(myDict) == len(mySet)

print(f"{uniqueOccurrences(caseArr_1)}")
print(f"{uniqueOccurrences(caseArr_2)}")
print(f"{uniqueOccurrences(caseArr_3)}")