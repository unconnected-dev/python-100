#Plus One
#https://leetcode.com/problems/plus-one/description/

caseDigits_1 = [1,2,3]
caseDigits_2 = [4,3,2,1]
caseDigits_3 = [9]
caseDigits_4 = [9,9]

if True:
    def plusOne(digits):
        
        rr_digits = digits[::-1]
        carry = False

        for i in range(len(digits)):
            if rr_digits[i] < 9:
                rr_digits[i] += 1
                carry = False
                break
            else:
                rr_digits[i] = 0
                carry = True

        if carry == True:
            rr_digits.append(1)

        return rr_digits[::-1]

print(f"{plusOne(caseDigits_1)}")
print(f"{plusOne(caseDigits_2)}")
print(f"{plusOne(caseDigits_3)}")
print(f"{plusOne(caseDigits_4)}")