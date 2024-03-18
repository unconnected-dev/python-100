#Jewels And Stones
#https://leetcode.com/problems/jewels-and-stones/description/
import collections

caseJewels_1 = "aA"
caseStones_1 = "aAAbbbb"

caseJewels_2 = "z"
caseStones_2 = "ZZ"

if False:
    def jewelsAndStones(jewels, stones):
        jewelSet = set(jewels)
        returnVal = 0

        for c in list(stones):
            if c in jewelSet:
                returnVal += 1

        return returnVal

if True:
    def jewelsAndStones(jewels, stones):
        jewel_counts = collections.Counter(jewels)        
        stone_counts = collections.Counter(stones)

        total = 0

        for key, value in stone_counts.items():
            if key in jewel_counts:
                total += value

        return total

print(f"{jewelsAndStones(caseJewels_1, caseStones_1)}")
print(f"{jewelsAndStones(caseJewels_2, caseStones_2)}")