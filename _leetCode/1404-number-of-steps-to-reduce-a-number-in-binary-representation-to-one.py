#Number Of Steps To Reduce A Number In Binary Representation To One
#https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/description/

caseS_1 = "1101"
caseS_2 = "10"
caseS_3 = "1"
caseS_4 = "1111011110000011100000110001011011110010111001010111110001"

if True:
    def numSteps(self, s: str) -> int:
        n = int(s, 2)
        res = 0

        while n != 1:
            if n%2 == 0:
                n //= 2
            else:
                n += 1
            
            res += 1


        return res
