#Count Good Triplets
#https://leetcode.com/problems/count-good-triplets/description/

caseArr_1 = [3,0,1,1,9,7]
caseA_1 = 7
caseB_1 = 2
caseC_1 = 3

caseArr_2 = [1,1,2,2,3]
caseA_2 = 0
caseB_2 = 0
caseC_2 = 1

caseArr_3 = [7,3,7,3,12,1,12,2,3]
caseA_3 = 5
caseB_3 = 8
caseC_3 = 1

if True:
    def countGoodTriplets(arr, a, b, c):
        count = 0
        l = len(arr)

        for i in range(0, l - 2):
            for j in range(i + 1, l - 1):
                for k in range(j + 1, l):
                    if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        count += 1
                        
        return count

print(f"{countGoodTriplets(caseArr_1, caseA_1, caseB_1, caseC_1)}")
print(f"{countGoodTriplets(caseArr_2, caseA_2, caseB_2, caseC_2)}")
print(f"{countGoodTriplets(caseArr_2, caseA_3, caseB_3, caseC_3)}")