#Counting Bits
#https://leetcode.com/problems/counting-bits/description/

caseN_1 = 2
caseN_2 = 5

if False:
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

if False:
    def countBits(n):
        res = []
        for i in range(n+1):
            res.append(len([c for c in bin(i) if c == "1"]))
            
        return res

#The solution has a pattern which allows for a solution using offset
#to check prior values and increment accordingly
# [0]
# [0, 1]
# [0, 1, 1, 2]
# [0, 1, 1, 2, 1, 2, 2, 3]
# [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4]
if True:
    def countBits(n):
        res = [0] * (n + 1)
        offset = 1
        for i in range(1, n + 1):
            if offset * 2 == i:
                offset *= 2
                
            res[i] = res[i - offset] + 1 

        return res
    
print(f"{countBits(caseN_1)}")
print(f"{countBits(caseN_2)}")