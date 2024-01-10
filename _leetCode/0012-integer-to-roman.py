#Integer To Roman
#https://leetcode.com/problems/integer-to-roman/description/


caseNum_1 = 3
caseNum_2 = 58
caseNum_3 = 1994

if True:
    def integerToRoman(num) -> str:
        m = [
            [1000, "M"],
            [900, "CM"],
            [500, "D"],
            [400, "CD"],
            [100, "C"],
            [90, "XC"],
            [50, "L"],
            [40, "XL"],
            [10, "X"],
            [9, "IX"],
            [5, "V"],
            [4, "IV"],
            [1, "I"],
        ]

        r = ""

        for [dn, str] in m:
            while (num/dn) >= 1:
                r += str
                num -=dn

        return r

print(f"{integerToRoman(caseNum_1)}")
print(f"{integerToRoman(caseNum_2)}")
print(f"{integerToRoman(caseNum_3)}")