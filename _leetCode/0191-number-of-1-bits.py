#Number Of 1 Bits
#https://leetcode.com/problems/number-of-1-bits/description/
import collections

caseN_1 = 11
caseN_2 = 128
caseN_3 = 4294967293

if False:
    def hammingWeight(n):
        count_ = collections.Counter(bin(n)[2:])
        return count_.get("1", 0)

if False:
    def hammingWeight(n):
        count = 0
        for c in bin(n)[2:]:
            if c == "1":
                count += 1

        return count

if True:
    def hammingWeight(n):
        return bin(n)[2:].count("1")

print(f"{hammingWeight(caseN_1)}")
print(f"{hammingWeight(caseN_2)}")
print(f"{hammingWeight(caseN_3)}")