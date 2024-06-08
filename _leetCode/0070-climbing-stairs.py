#Climbing Stairs
#https://leetcode.com/problems/climbing-stairs/description/

caseN_1 = 2
caseN_2 = 3
caseN_3 = 44

#Time Limit Exceeded
if True:
    def climbStairs(n):
        
        if n == 0 or n == 1:
            return 1
        
        return climbStairs(n-1) + climbStairs(n-2)

print(f"{climbStairs(caseN_1)}")
print(f"{climbStairs(caseN_2)}")
print(f"{climbStairs(caseN_3)}")