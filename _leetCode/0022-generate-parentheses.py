#Generate Parentheses
#https://leetcode.com/problems/generate-parentheses/description/

caseN_1 = 3
caseN_2 = 1

if True:
    def generateParenthesis(n):
        stack = []
        res = []
        
        def backtrack(openN, closeN):
            if openN == closeN == n:
                res.append(''.join(stack))
                return
        
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closeN)
                stack.pop()
            
            if closeN < openN:
                stack.append(")")
                backtrack(openN, closeN + 1)
                stack.pop()
        
        backtrack(0, 0)
        return res

print(f"{generateParenthesis(caseN_1)}")
print(f"{generateParenthesis(caseN_2)}")