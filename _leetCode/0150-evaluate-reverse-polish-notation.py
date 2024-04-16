#Evaluate Reverse Polish Notation
#https://leetcode.com/problems/evaluate-reverse-polish-notation/description/

caseTokens_1 = ["2","1","+","3","*"]
caseTokens_2 = ["4","13","5","/","+"]
caseTokens_3 = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

if False:
    def evalRPN(tokens):
        stack = []
        
        def is_number(c):
            try:
                int(c)
                return True
            except ValueError:
                return False

        
        for t in tokens:
            if is_number(t):
                stack.append(int(t))
            else:
                b = stack.pop()
                a = stack.pop()
                
                match t:
                    case "+":
                        stack.append(a+b)
                    case "-":
                        stack.append(a-b)
                    case "/":
                        #int will convert to whole number and round towards 0
                        stack.append(int(a/b))
                    case "*":
                        stack.append(a*b)
        
        return stack[-1]

if True:
    def evalRPN(tokens):
        stack = []
        ops = "+-*/"
        for t in tokens:
            if t not in ops:
                stack.append(int(t))
            else:
                b, a = stack.pop(), stack.pop()
                
                if t == "+":    stack.append(a+b)
                elif t == "-":    stack.append(a-b)
                elif t == "*":    stack.append(a*b)
                elif t == "/":    stack.append(int(a/b))
        
        return stack[-1]

print(f"{evalRPN(caseTokens_1)}")
print(f"{evalRPN(caseTokens_2)}")
print(f"{evalRPN(caseTokens_3)}")