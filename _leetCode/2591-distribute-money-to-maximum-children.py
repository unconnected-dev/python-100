#Distribute Money To Maximum Children
#https://leetcode.com/problems/distribute-money-to-maximum-children/description/

import math

caseMoney_1 = 20
caseChildren_1 =  3

caseMoney_2 = 16
caseChildren_2 = 2

if True:
    def distMoney(money, children):
        if children * 8 == money:
            return children
        elif children * 8 < money:
            return children - 1
        elif money < children or (money == 4 and children == 1):
            return -1
        elif money == children:
            return 0
        
        initial_handout = money - children
        with8 = math.floor(initial_handout / 7)
        money_remaining = initial_handout % 7

        if money_remaining == 3 and with8 > 0 and children - with8 == 1:
            with8 -= 1
        
        return with8

print(f"{distMoney(caseMoney_1, caseChildren_1)}")
print(f"{distMoney(caseMoney_2, caseChildren_2)}")