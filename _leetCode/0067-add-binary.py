#Add Binary
#https://leetcode.com/problems/add-binary/description/

caseA_1 = "11"
caseB_1 = "1"

caseA_2 = "1010"
caseB_2 = "1011"

if False:
    def addBinary(a, b) -> str:
        sum = bin(int(a, 2) + int(b, 2))
        return sum[2:]

if True:
    def addBinary(a, b) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]

print(f"{addBinary(caseA_1, caseB_1)}")
print(f"{addBinary(caseA_2, caseB_2)}")