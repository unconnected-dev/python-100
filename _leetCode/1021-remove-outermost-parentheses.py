#Remove Outermost Parentheses
#https://leetcode.com/problems/remove-outermost-parentheses/description/

caseS_1 = "(()())(())"
caseS_2 = "(()())(())(()(()))"
caseS_3 = "()()"

if True:
    def removeOuterParentheses(s):
        res = []
        
        open, close = 0, 0
        temp = ""
        for c in s:
            if c == "(":
                open += 1
            else:
                close += 1
            
            temp += c    
            if open == close:
                res.append(temp[1:-1])
                temp = ""
                open = 0
                close = 0
                        
        return ''.join(res)
    
print(f"{removeOuterParentheses(caseS_1)}")
print(f"{removeOuterParentheses(caseS_2)}")
print(f"{removeOuterParentheses(caseS_3)}")