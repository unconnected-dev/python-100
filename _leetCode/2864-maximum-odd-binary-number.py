#Maximum Odd Binary Number
#https://leetcode.com/problems/maximum-odd-binary-number/description/

caseS_1 = "010"
caseS_2 = "0101"

if True:
    def maximumOddBinaryNumber(s):
        ones = []
        zeroes = []

        for c in s:
            if c == '1':
                ones.append(c)
            else:
                zeroes.append(c)

        if ones == 1:
            return ''.join(zeroes) + ''.join(ones)
        else:
            return ''.join(ones[1:]) + ''.join(zeroes) + '1'

print(f"{maximumOddBinaryNumber(caseS_1)}")
print(f"{maximumOddBinaryNumber(caseS_2)}")