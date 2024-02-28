#Percentage Of Letter In String
#https://leetcode.com/problems/percentage-of-letter-in-string/description/
import math

caseS_1 = "foobar"
caseLetter_1 = "o"

caseS_2 = "jjjj"
caseLetter_2 = "k"

if False:
    def percentageLetter(s, letter):
        c = s.count(letter)
        return math.floor(c/len(s) * 100)

if True:
    def percentageLetter(s, letter):
        return math.floor(s.count(letter)/len(s) * 100)

print(f"{percentageLetter(caseS_1, caseLetter_1)}")
print(f"{percentageLetter(caseS_2, caseLetter_2)}")