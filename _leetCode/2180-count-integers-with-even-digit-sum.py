#Count Integers With Even Digit Sum
#https://leetcode.com/problems/count-integers-with-even-digit-sum/description/

caseNum_1 = 4
caseNum_2 = 30

if False:
    def get_digit_sum(num):
        return sum(int(digit) for digit in str(num))
    
    def countEven(num):
        c = 0

        for i in range(1, num + 1):
            if get_digit_sum(i) % 2 == 0:
                c += 1

        return c

if False:
    def countEven(num):
        c = 0
        
        for i in range(1, num + 1):
            digit_sum = sum(int(digit) for digit in str(i))
            if digit_sum % 2 == 0 and digit_sum != 0:
                c += 1

        return c

if True:
    def countEven(num):
        f = lambda x: sum(int(d) for d in str(x)) % 2 == 0
        nums_sum = [n for n in range(1, num + 1) if f(n)]

        return len(nums_sum)

print(f"{countEven(caseNum_1)}")
print(f"{countEven(caseNum_2)}")