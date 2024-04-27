#Maximum Ice Cream Bars
#https://leetcode.com/problems/maximum-ice-cream-bars/description/

caseCosts_1 = [1,3,2,4,1]
caseCoins_1 = 7

caseCosts_2 = [10,6,8,7,7,8]
caseCoins_2 = 5

caseCosts_3 = [1,6,3,1,2,5]
caseCoins_3 = 20

if True:
    def maxIceCream(costs, coins):
        max_cost = max(costs)

        costs_counted = [0]*(max_cost + 1)
        res = 0

        for c in costs:
            costs_counted[c] += 1
        
        for i in range(len(costs_counted)):
            
            while costs_counted[i] > 0 and (coins > 0 and coins >= i):
                costs_counted[i] -= 1
                coins -= i
                res += 1
            
            if coins == 0 or coins < i:
                break

        return res

print(f"{maxIceCream(caseCosts_1, caseCoins_1)}")
print(f"{maxIceCream(caseCosts_2, caseCoins_2)}")
print(f"{maxIceCream(caseCosts_3, caseCoins_3)}")