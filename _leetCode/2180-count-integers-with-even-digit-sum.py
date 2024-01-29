#Count Integers With Even Digit Sum
#https://leetcode.com/problems/count-integers-with-even-digit-sum/description/

caseNum_1 = 4
caseNum_2 = 30

if True:
    def get_digit_sum(num):
        return sum(int(digit) for digit in str(num))
    
    def countEven(num):
        c = 0

        for i in range(1, num + 1):
            if get_digit_sum(i) % 2 == 0:
                c += 1

        return c


print(f"{countEven(caseNum_1)}")
print(f"{countEven(caseNum_2)}")