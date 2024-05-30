#Find Lucky Integer In An Array
#https://leetcode.com/problems/find-lucky-integer-in-an-array/description/

from typing import Counter


caseArr_1 = [2,2,3,4]
caseArr_2 = [1,2,2,3,3,3]
caseArr_3 = [2,2,2,3,3]

if False:
    def findLucky(arr):
        my_dict = {}

        for n in arr:
            my_dict[n] = my_dict.get(n, 0) + 1
        
        res = -1
        for k, v in my_dict.items():
            if k == v:
                res = max(res, k)

        return res

if False:
    def findLucky(arr):
        count = Counter(arr)
        res = [k if k == v else -1 for k, v in count.items()]
        return max(res)

if True:
    def findLucky(arr):
        my_dict = {}

        for n in arr:
            my_dict[n] = my_dict.get(n, 0) + 1
        
        res = [k if k == v else -1 for k, v in my_dict.items()]

        return max(res)
        
print(f"{findLucky(caseArr_1)}")
print(f"{findLucky(caseArr_2)}")
print(f"{findLucky(caseArr_3)}")