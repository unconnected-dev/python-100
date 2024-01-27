#Sum Of All Odd Length Subarrays
#https://leetcode.com/problems/sum-of-all-odd-length-subarrays/description/

caseArr_1 = [1,4,2,5,3]
caseArr_2 = [1,2]
caseArr_3 = [10,11,12]

if True:
    def sumOddLengthSubarrays(arr):
        o = 1
        returnNumber = 0

        while o <= len(arr):
            for i in range(len(arr)):
                if (i + o) < (len(arr) + 1):
                    for j in range(i, i + o):
                        returnNumber += arr[j]
            o += 2
        
        return returnNumber

print(f"{sumOddLengthSubarrays(caseArr_1)}")
print(f"{sumOddLengthSubarrays(caseArr_2)}")
print(f"{sumOddLengthSubarrays(caseArr_3)}")