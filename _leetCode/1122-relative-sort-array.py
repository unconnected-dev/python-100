#Relative Sort Array
#https://leetcode.com/problems/relative-sort-array/description/

caseArr1_1 = [2,3,1,3,2,4,6,7,9,2,19]
caseArr2_1 = [2,1,4,3,9,6]

caseArr1_2 = [28,6,22,8,44,17]
caseArr2_2 = [22,28,8,6]

if False:
    def relativeSortArray(arr1, arr2):
        mySet = set(arr2)
        inList = []
        extraList = []

        for val in arr1:
            if val in mySet:
                inList.append(val)
            else:
                extraList.append(val)

        extraList.sort()

        inList.sort(key = lambda x: arr2.index(x))

        for val in extraList:
            inList.append(val)

        return inList

if True:
    def relativeSortArray(arr1, arr2):
        return_lst = []    

        for n in arr2:
            while n in arr1:
                return_lst.append(n)
                arr1.remove(n)

        return return_lst + sorted(arr1) 

print(f"{relativeSortArray(caseArr1_1, caseArr2_1)}")
print(f"{relativeSortArray(caseArr2_1, caseArr2_2)}")