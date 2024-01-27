#Determine Color Of A Chessboard Square
#https://leetcode.com/problems/determine-color-of-a-chessboard-square/description/

caseCoordinates_1 = "a1"
caseCoordinates_2 = "h3"
caseCoordinates_3 = "c7"

if False:
    def squareIsWhite(coordinates):
        letters = "abcdefgh"
        ind = letters.index(coordinates[0])
        n = int(coordinates[1])

        if ((ind + 1) + n) % 2 == 0:
            return False
        else:
            return True

if True:
    def squareIsWhite(coordinates):
        letters = "abcdefgh"
        return (letters.index(coordinates[0]) + 1 + int(coordinates[1])) % 2 != 0

print(f"{squareIsWhite(caseCoordinates_1)}")
print(f"{squareIsWhite(caseCoordinates_2)}")
print(f"{squareIsWhite(caseCoordinates_3)}")
