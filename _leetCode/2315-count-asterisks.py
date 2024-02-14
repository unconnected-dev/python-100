#Count Asterisks
#https://leetcode.com/problems/count-asterisks/description/

caseS_1 = "l|*e*et|c**o|*de|"
caseS_2 = "iamprogrammer"
caseS_3 = "yo|uar|e**|b|e***au|tifu|l"

if True:
    def countAsterisks(s) -> int:
        count = 0
        outsidePairs = True

        for c in s:
            if c == "|":
                outsidePairs = not outsidePairs
            elif outsidePairs == True and c == "*":
                count += 1

        return count

print(f"{countAsterisks(caseS_1)}")
print(f"{countAsterisks(caseS_2)}")
print(f"{countAsterisks(caseS_3)}")