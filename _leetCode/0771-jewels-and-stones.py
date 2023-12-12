#Jewels And Stones
#https://leetcode.com/problems/jewels-and-stones/description/

caseJewels_1 = "aA"
caseStones_1 = "aAAbbbb"

caseJewels_2 = "z"
caseStones_2 = "ZZ"

if True:
    def jewelsAndStones(jewels, stones):
        jewelSet = set(jewels)
        returnVal = 0

        for c in list(stones):
            if c in jewelSet:
                returnVal += 1

        print(f"return {returnVal}")

    jewelsAndStones(caseJewels_1, caseStones_1)
    jewelsAndStones(caseJewels_2, caseStones_2)