#Difference Between Element Sum And Digit Sum Of An Array
#https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/description/

caseNums_1 = [1,15,6,3]
caseNums_2 = [1,2,3,4]

if True:
    def differenceOfSum(nums):
        digits_sum = sum(int(digit) for digit in ''.join(map(str, nums)))
        return sum(nums) - digits_sum

print(f"{differenceOfSum(caseNums_1)}")
print(f"{differenceOfSum(caseNums_2)}")