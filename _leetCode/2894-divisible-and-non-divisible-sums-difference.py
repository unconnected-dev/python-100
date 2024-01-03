#Divisible And Non-Divisible Sums Difference
#https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/description/

caseN_1 = 10
caseM_1 = 3

caseN_2 = 5
caseM_2 = 6

caseN_3 = 5
caseM_3 = 1

if True:
    def differenceOfSums(n, m) -> int:
        sum = 0

        for i in range(1, n + 1):
            if i % m == 0:
                sum -= i
            else:
                sum += i
        
        return sum
    
print(f"{differenceOfSums(caseN_1, caseM_1)}")
print(f"{differenceOfSums(caseN_2, caseM_2)}")
print(f"{differenceOfSums(caseN_3, caseM_3)}")