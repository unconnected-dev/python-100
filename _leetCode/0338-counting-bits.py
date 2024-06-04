#Counting Bits
#https://leetcode.com/problems/counting-bits/description/

caseN_1 = 2
caseN_2 = 5

if True:
    def countBits(n):
        res = []
        for i in range(n+1):
            b = bin(i)[2:]
            br = 0
            for c in b:
                if c == "1":
                    br += 1

            res.append(br)
        return res

print(f"{countBits(caseN_1)}")
print(f"{countBits(caseN_2)}")