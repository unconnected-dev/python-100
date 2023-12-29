#Number Of Steps To Reduce A Number To Zero
#https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/description/

caseNums_1 = 14
caseNums_2 = 8
caseNums_3 = 123

if True:
    def numberOfSteps(num):
        steps = 0

        while num != 0 and num > 0:
            if num % 2 == 1:
                num -= 1
            else:
                num /= 2
            
            steps += 1

        return steps

print(f"{numberOfSteps(caseNums_1)}")
print(f"{numberOfSteps(caseNums_2)}")
print(f"{numberOfSteps(caseNums_3)}")