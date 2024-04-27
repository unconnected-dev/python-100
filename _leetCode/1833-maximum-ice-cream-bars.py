#Maximum Ice Cream Bars
#https://leetcode.com/problems/maximum-ice-cream-bars/description/

caseCosts_1 = [1,3,2,4,1]
caseCoins_1 = 7

caseCosts_2 = [10,6,8,7,7,8]
caseCoins_2 = 5

caseCosts_3 = [1,6,3,1,2,5]
caseCoins_3 = 20

if False:
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

if False:
    def maxIceCream(costs, coins):
        res = 0
        costs.sort()
        for i in costs:
            if i <= coins:
                coins -= i
                res += 1
            else:
                break

        return res

if False:
    def maxIceCream(costs, coins):
        costs.sort(reverse=True)
        res = 0
        while coins > 0 and costs:
            cost = costs.pop()
            if cost <= coins:
                coins -= cost
                res += 1
            else:
                break
        
        return res

if True:
    def maxIceCream(costs, coins):
        max_cost = max(costs)
        my_dict = {}
        res = 0

        for n in range(max_cost):
            my_dict[n] = 0
        
        for c in costs:
            my_dict[c] = my_dict.get(c, 0) + 1
        
        for key, val in my_dict.items():
            while coins >= key and val > 0:
                coins -= key
                val -= 1
                res += 1

            if val > 0:
                break

        return res    

print(f"{maxIceCream(caseCosts_1, caseCoins_1)}")
print(f"{maxIceCream(caseCosts_2, caseCoins_2)}")
print(f"{maxIceCream(caseCosts_3, caseCoins_3)}")