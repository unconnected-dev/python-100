#Minimum Sum Of Four Digit Number After Splitting Digits
#https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/description/

caseNum_1 = 2932
caseNum_2 = 4009

if True:
    def minimumSum(num):
        num_str = str(num)
        num_s = sorted(num_str, key=lambda x: int(x))

        result = int(num_s[0] + num_s[2]) + int(num_s[1] + num_s[3])
        return result

print(f"{minimumSum(caseNum_1)}")
print(f"{minimumSum(caseNum_2)}")