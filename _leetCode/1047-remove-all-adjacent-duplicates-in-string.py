#Remove All Adjacent Duplicates In String
#https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/description/

caseS_1 = "abbaca"
caseS_2 = "azxxzy"

if True:
    def removeDuplicates(s):
        stack = []
        
        for c in s:
            if stack and stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)
                
        return ''.join(stack)                
    
print(f"{removeDuplicates(caseS_1)}")
print(f"{removeDuplicates(caseS_2)}")