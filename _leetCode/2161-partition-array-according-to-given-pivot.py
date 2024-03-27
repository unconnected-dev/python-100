#Partition Array According To Given Pivot
#https://leetcode.com/problems/partition-array-according-to-given-pivot/description/

caseNums_1 = [9,12,5,10,14,3,10]
casePivot_1 = 10

caseNums_2 = [-3,4,3,2]
casePivot_2 = 2

if False:
    def pivotArray(nums, pivot):
        left, mid, right = [], [], []

        for n in nums:
            if n < pivot:
                left.append(n)
            elif n > pivot:
                right.append(n)
            else:
                mid.append(pivot)

        return left + mid + right

if True:
    def pivotArray(nums, pivot):
        left = [n for n in nums if n < pivot]
        mid = [n for n in nums if n == pivot]
        right = [n for n in nums if n > pivot]
        
        return left + mid + right

print(f"{pivotArray(caseNums_1, casePivot_1)}")
print(f"{pivotArray(caseNums_2, casePivot_2)}")