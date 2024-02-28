#Nim Game
#https://leetcode.com/problems/nim-game/description/

caseN_1 = 4
caseN_2 = 1
caseN_3 = 2

if True:
    def canWinNim(n):
        return n % 4 != 0

print(f"{canWinNim(caseN_1)}")
print(f"{canWinNim(caseN_2)}")
print(f"{canWinNim(caseN_3)}")