#Number Of Steps To Reduce A Number In Binary Representation To One
#https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/description/

caseS_1 = "1101"
caseS_2 = "10"
caseS_3 = "1"
caseS_4 = "1111011110000011100000110001011011110010111001010111110001"

if False:
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

if True:
    def numSteps(self, s: str) -> int:
        steps, carry = 0, 0

        for i in range(len(s)-1,0,-1):
            if s[i] == "0":
                if carry:
                    steps += 2
                else:
                    steps += 1
            else:
                if carry:
                    steps += 1
                else:
                    steps += 2
                    carry = 1
        
        return steps + carry

print(f"{numSteps(caseS_1)}")
print(f"{numSteps(caseS_2)}")
print(f"{numSteps(caseS_3)}")
print(f"{numSteps(caseS_4)}")