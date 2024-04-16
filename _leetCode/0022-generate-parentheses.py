#Generate Parentheses
#https://leetcode.com/problems/generate-parentheses/description/

caseN_1 = 3
caseN_2 = 1

if False:
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

if False:
    def generateParenthesis(n):
        stack = []
        res = []
        
        def backtrack(left, right):
            if left == right == n:
                res.append(''.join(stack))
                return
        
            if left < n:
                stack.append("(")
                backtrack(left + 1, right)            
                stack.pop()
            
            if right < left:
                stack.append(")")
                backtrack(left, right + 1)
                stack.pop()
        
        backtrack(0, 0)
        return res
    
if True:
    def generateParenthesis(n):
        res = []

        def backtrack(left, right, path):
            if left == right == n:
                res.append(path)
                return

            if left < n:
                backtrack(left + 1, right, path + "(")
            
            if right < left:
                backtrack(left, right + 1, path + ")")
        
        backtrack(0 ,0, "")
        return res
    
print(f"{generateParenthesis(caseN_1)}")
print(f"{generateParenthesis(caseN_2)}")