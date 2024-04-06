#Subtract The Product And Sum Of Digits Of An Integer
#https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/description/

caseNum_1 = 234
caseNum_2 = 4421

if False:
    def subtractProductAndSum(n) -> int:
        na = str(n)
        pro = 1
        sum = 0

        for i in range(len(na)):
            val = int(na[i])
            pro *= val
            sum += val

        return pro - sum

if True:
    def subtractProductAndSum(n) -> int:
        pro, sum = 1, 0

        while n > 0:
            pro *= n%10
            sum += n%10
            n //= 10

        return pro - sum

print(f"{subtractProductAndSum(caseNum_1)}")
print(f"{subtractProductAndSum(caseNum_2)}")