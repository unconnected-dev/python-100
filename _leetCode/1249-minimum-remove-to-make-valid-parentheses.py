#Minimum Remove To Make Valid Parentheses
#https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/description/

caseS_1 = "lee(t(c)o)de)"
caseS_2 = "a)b(c)d"
caseS_3 = "))(("
caseS_4 = "())()((("

if False:
    def minRemoveToMakeValid(s):
        s_list= [*s]
        count = 0
        res_list = []
        
        for c in s_list:
            if c == ")" and count <= 0:
                continue
            elif c == "(":
                count += 1
            elif c == ")":
                count -= 1
                
            res_list.append(c)
            
        right = len(res_list) -1
        while count > 0:
            if res_list[right] == "(":
                res_list.pop(right)
                count -= 1
                
            right -= 1
            
        return ''.join(res_list)

if True:
    def minRemoveToMakeValid(s):
        sl = list(s)
        stack = []
        
        for i, c in enumerate(sl):
            if c == "(":
                stack.append(i)
            elif c == ")":
                if stack:
                    stack.pop()
                else:
                    sl[i] = ''
                    
        for i in stack:
            sl[i] = ''
        
        return ''.join(sl)

print(f"{minRemoveToMakeValid(caseS_1)}")
print(f"{minRemoveToMakeValid(caseS_2)}")
print(f"{minRemoveToMakeValid(caseS_3)}")
print(f"{minRemoveToMakeValid(caseS_4)}")