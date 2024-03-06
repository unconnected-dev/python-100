#Roman To Integer
#https://leetcode.com/problems/roman-to-integer/description/

caseString_1 = "III"
caseString_2 = "LVIII"
caseString_3 = "MCMXCIV"

if False:
    def romanToInteger(s) -> int:
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
        
        return result

if False:
    def romanToInteger(s) -> int:
        numerals = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        s = s.replace("IV","IIII").replace("IX","VIIII")
        s = s.replace("XL","XXXX").replace("XC","LXXXX")
        s = s.replace("CD","CCCC").replace("CM","DCCCC")

        result = 0
        for c in s:
            result += numerals[c]

        return result

if True:
    def romanToInteger(s) -> int:
        numerals = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV" : -2,
            "IX" : -2,
            "XL" : -20,
            "XC" : -20,
            "CD" : -200,
            "CM" : -200
        }

        result = 0
        for numeral, val in numerals.items():
            if numeral in s:
                result += val * s.count(numeral)
        
        return result

print(f"{romanToInteger(caseString_1)}")    
print(f"{romanToInteger(caseString_2)}")    
print(f"{romanToInteger(caseString_3)}")    