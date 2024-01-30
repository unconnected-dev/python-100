#Find The Pivot Integer
#https://leetcode.com/problems/find-the-pivot-integer/description/

caseNum_1 = 8
caseNum_2 = 1
caseNum_3 = 4

if True:
    def pivotInteger(n):
        total = 0

        for i in range(1, n + 1):
            total += i

        left = 0
        right = 0

        for i in range(1, n + 1):
            left += i
            right = total - left

            if left == right + i:
                return i
            
        return -1

print(f"{pivotInteger(caseNum_1)}")
print(f"{pivotInteger(caseNum_2)}")
print(f"{pivotInteger(caseNum_3)}")