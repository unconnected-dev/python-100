#Water Bottles
#https://leetcode.com/problems/water-bottles/description/

import math

caseNumBottles_1 = 9
caseNumExchange_1 = 3

caseNumBottles_2 = 15
caseNumExchange_2 = 4

if True:
    def waterBottles(numBottles, numExhange):
        total = numBottles
        emptyBottles = numBottles

        while emptyBottles >= numExhange:
            remainder = emptyBottles % numExhange
            numBottles = math.floor(emptyBottles / numExhange)

            total += numBottles
            emptyBottles = numBottles + remainder
        
        return total
    
    print(f"{waterBottles(caseNumBottles_1, caseNumExchange_1)}")
    print(f"{waterBottles(caseNumBottles_2, caseNumExchange_2)}")