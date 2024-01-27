#Calculate Money In Leetcode Bank
#https://leetcode.com/problems/calculate-money-in-leetcode-bank/description/

caseNum_1 = 4
caseNum_2 = 10
caseNum_3 = 20

if True:
    def totalMoney(n):
        total = 0
        daily = 1
        week = 1

        for i in range(1, n+1):
            total += daily
            daily += 1

            if i % 7 == 0:
                daily = week + 1
                week += 1
        
        return total

print(f"{totalMoney(caseNum_1)}")
print(f"{totalMoney(caseNum_2)}")
print(f"{totalMoney(caseNum_3)}")