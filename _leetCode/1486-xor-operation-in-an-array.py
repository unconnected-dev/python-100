#XOR Operation In An Array
#https://leetcode.com/problems/xor-operation-in-an-array/description/

caseN_1 = 5
caseStart_1 = 0

caseN_2 = 4
caseStart_2 = 3

if True:
    def xorOperation(n, start):
        res = 0
        for i in range(n):
            res ^= start + 2 * i
        return res
    
print(f"{xorOperation(caseN_1, caseStart_1)}")
print(f"{xorOperation(caseN_2, caseStart_2)}")