#Baseball Game
#https://leetcode.com/problems/baseball-game/description/

caseOperations_1 = ["5","2","C","D","+"]
caseOperations_2 = ["5","-2","4","C","D","9","+","+"]
caseOperations_3 = ["1","C"]

if True:
    def calPoints(operations):
        stack = []
        
        for o in operations:
            if o == "+":
                stack.append(stack[-1] + stack[-2])
            elif o == "D":
                stack.append(stack[-1] * 2)
            elif o == "C":
                stack.pop()
            else:
                stack.append(int(o))

        return sum(stack)
        
print(f"{calPoints(caseOperations_1)}")
print(f"{calPoints(caseOperations_2)}")
print(f"{calPoints(caseOperations_3)}")