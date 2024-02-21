#Reduce Array Size To The Half
#https://leetcode.com/problems/reduce-array-size-to-the-half/description/

from collections import Counter


caseArr_1 = [3,3,3,3,5,5,5,2,2,7]
caseArr_2 = [7,7,7,7,7,7]

if True:
    def minSetSize(arr):
        half_length = len(arr)//2

        arr_dict = Counter(arr).items()
        sorted_arr_dict = sorted(arr_dict, key=lambda item: -item[1])

        running_total = 0
        result = 0
        for item in sorted_arr_dict:
            running_total += item[1]
            result += 1
            
            if running_total >= half_length:
                break
        
        return result

print(f"{minSetSize(caseArr_1)}")
print(f"{minSetSize(caseArr_2)}")