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
        ind = letters.index(coordinates[0])
        n = int(coordinates[1])

        return ((ind + 1) + n) % 2 != 0

if False:
    def squareIsWhite(coordinates):
        letters = "abcdefgh"
        return (letters.index(coordinates[0]) + 1 + int(coordinates[1])) % 2 != 0

if False:
    def squareIsWhite(coordinates):
        my_dict = {
            "a":1,
            "b":2,
            "c":3,
            "d":4,
            "e":5,
            "f":6,
            "g":7,
            "h":8
        }

        return (my_dict.get(coordinates[0], 0) + int(coordinates[1])) % 2 != 0

if True:
    def squareIsWhite(coordinates):
        my_set = (["a","c","e","g"])

        if coordinates[0] in my_set:
            return int(coordinates[1])%2 == 0
        else:
            return int(coordinates[1])%2 == 1

print(f"{squareIsWhite(caseCoordinates_1)}")
print(f"{squareIsWhite(caseCoordinates_2)}")
print(f"{squareIsWhite(caseCoordinates_3)}")
