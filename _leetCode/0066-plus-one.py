#Plus One
#https://leetcode.com/problems/plus-one/description/

caseDigits_1 = [1,2,3]
caseDigits_2 = [4,3,2,1]
caseDigits_3 = [9]
caseDigits_4 = [9,9]

if False:
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

if False:
    def plusOne(digits):
        reverse_digits = digits[::-1]
        digits_length = len(digits)
        carry_one = False
        i = 0
        while i < digits_length:
            if reverse_digits[i] < 9:
                reverse_digits[i] += 1
                carry_one = False
                break
            else:
                reverse_digits[i] = 0
                carry_one = True

            i += 1

        if carry_one == True:
            reverse_digits.append(1)

        return reverse_digits[::-1]

if True:
    def plusOne(digits):
        digits_length = len(digits)

        for i in range(digits_length-1,-1,-1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
            
        return [1] + digits

print(f"{plusOne(caseDigits_1)}")
print(f"{plusOne(caseDigits_2)}")
print(f"{plusOne(caseDigits_3)}")
print(f"{plusOne(caseDigits_4)}")