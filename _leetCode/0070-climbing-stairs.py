#Climbing Stairs
#https://leetcode.com/problems/climbing-stairs/description/

caseN_1 = 2
caseN_2 = 3
caseN_3 = 44

#Time Limit Exceeded
if False:
    def climbStairs(n):
        
        if n == 0 or n == 1:
            return 1
        
        return climbStairs(n-1) + climbStairs(n-2)

#Memorization
if True:
    class Solution:
        def climbStairs(self, n: int) -> int:
            memo = {}
            return self.helper(n , memo)
        
        def helper(self, n, memo):

            if n == 0 or n == 1:
                return 1
            
            if n not in memo:
                memo[n] = self.helper(n-1, memo) + self.helper(n-2, memo)
            
            return memo[n]

sol = Solution()

print(f"{sol.climbStairs(caseN_1)}")
print(f"{sol.climbStairs(caseN_2)}")
print(f"{sol.climbStairs(caseN_3)}")