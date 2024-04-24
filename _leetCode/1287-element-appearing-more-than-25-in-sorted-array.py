#Element Appearing More Than 25% In Sorted Array
#https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/description/

caseArr_1 = [1,2,2,6,6,6,6,7,10]
caseArr_2 = [1,1]
caseArr_3 = [1,2,3,3]

if True:
    def findSpecialInteger(arr):
        my_dict = {}
        target = len(arr)/4
        
        for n in arr:
            my_dict[n] = my_dict.get(n, 0) + 1
            if my_dict.get(n) > target:
                return n
    
print(f"{findSpecialInteger(caseArr_1)}")
print(f"{findSpecialInteger(caseArr_2)}")
print(f"{findSpecialInteger(caseArr_3)}")