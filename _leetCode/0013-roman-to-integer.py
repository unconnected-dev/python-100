#Roman To Integer
#https://leetcode.com/problems/roman-to-integer/description/

testCase1 = "III"
testCase2 = "LVIII"
testCase3 = "MCMXCIV"

def romanToInteger(s):
    numerals = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    stringList = list(s)
    result = 0

    for i in range(len(stringList)):
        c = numerals[stringList[i]]

        if i + 1 < len(stringList) and c < numerals[stringList[i + 1]]:
            result -= c
        else:
            result += c
    
    print(f"result: {result}")

romanToInteger(testCase1)
romanToInteger(testCase2)
romanToInteger(testCase3)