#Sum Multiples
#https://leetcode.com/problems/sum-multiples/description/

caseNum_1 = 7
caseNum_2 = 10
caseNum_3 = 9

if True:
    def sumMultiples(num) -> int:
        sum = 0 

        for i in range(1, num + 1):
            if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
                sum += i
        
        return sum

print(f"{sumMultiples(caseNum_1)}")
print(f"{sumMultiples(caseNum_2)}")
print(f"{sumMultiples(caseNum_3)}")