#Water Bottles
#https://leetcode.com/problems/water-bottles/description/

import math

caseNumBottles_1 = 9
caseNumExchange_1 = 3

caseNumBottles_2 = 15
caseNumExchange_2 = 4

if False:
    def waterBottles(numBottles, numExchange) -> int:
        total = numBottles
        emptyBottles = numBottles

        while emptyBottles >= numExchange:
            remainder = emptyBottles % numExchange
            numBottles = math.floor(emptyBottles / numExchange)

            total += numBottles
            emptyBottles = numBottles + remainder
        
        return total

if True:
    def waterBottles(numBottles, numExchange) -> int:
        total = numBottles

        while numBottles >= numExchange:
            numBottles, remainder = divmod(numBottles, numExchange)
            total += numBottles
            numBottles += remainder

        return total

print(f"{waterBottles(caseNumBottles_1, caseNumExchange_1)}")
print(f"{waterBottles(caseNumBottles_2, caseNumExchange_2)}")