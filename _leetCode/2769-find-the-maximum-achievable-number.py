#Find The Maximum Achievable Number
#https://leetcode.com/problems/find-the-maximum-achievable-number/description/

caseNum_1 = 4 
caseT_1 = 1

caseNum_2 = 3
caseT_2 = 2

if True:
    def theMaximumAchievableX(num, t) -> int:
        return num + (t * 2)

print(f"{theMaximumAchievableX(caseNum_1, caseT_1)}")
print(f"{theMaximumAchievableX(caseNum_2, caseT_2)}")