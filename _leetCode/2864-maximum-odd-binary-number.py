#Maximum Odd Binary Number
#https://leetcode.com/problems/maximum-odd-binary-number/description/
import collections

caseS_1 = "010"
caseS_2 = "0101"

if False:
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

if True:
    def maximumOddBinaryNumber(s):
        sl = list(s)

        left = 0
        for right in range(len(sl)):
            if sl[right] == '1':
                sl[right], sl[left] = sl[left], sl[right]
                left+=1

        sl[left-1], sl[-1] = sl[-1], sl[left-1]

        return ''.join(sl)


print(f"{maximumOddBinaryNumber(caseS_1)}")
print(f"{maximumOddBinaryNumber(caseS_2)}")