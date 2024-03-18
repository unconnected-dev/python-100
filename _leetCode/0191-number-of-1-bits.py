#Number Of 1 Bits
#https://leetcode.com/problems/number-of-1-bits/description/
import collections

caseN_1 = 11
caseN_2 = 128
caseN_3 = 4294967293

if True:
    def hammingWeight(n):
        count_ = collections.Counter(bin(n)[2:])
        return count_.get("1", 0)

print(f"{hammingWeight(caseN_1)}")
print(f"{hammingWeight(caseN_2)}")
print(f"{hammingWeight(caseN_3)}")