#Subtract The Product And Sum Of Digits Of An Integer
#https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/description/

caseNum_1 = 234
caseNum_2 = 4421

if True:
    def subtractProductAndSum(num) -> int:
        na = str(num)
        pro = 1
        sum = 0

        for i in range(len(na)):
            val = int(na[i])
            pro *= val
            sum += val

        return pro - sum

print(f"{subtractProductAndSum(caseNum_1)}")
print(f"{subtractProductAndSum(caseNum_2)}")