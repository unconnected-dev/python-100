#Maximum 69 Number
#https://leetcode.com/problems/maximum-69-number/description/

caseNum_1 = 9669
caseNum_2 = 9996
caseNum_3 = 9999

if True:
    def maximum69Number(num) -> int:
        return str(num).replace('6','9', 1)

print(f"{maximum69Number(caseNum_1)}")
print(f"{maximum69Number(caseNum_2)}")
print(f"{maximum69Number(caseNum_3)}")