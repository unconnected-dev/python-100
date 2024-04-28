#Backspace String Compare
#https://leetcode.com/problems/backspace-string-compare/description/

caseS_1 = "ab#c"
caseT_1 = "ad#c"

caseS_2 = "ab##"
caseT_2 = "c#d#"

caseS_3 = "a#c"
caseT_3 = "b"

caseS_4 = "y#fo##f"
caseT_4 = "y#f#o##f"

if True:
    def backspaceCompare(s, t):
        s_stack = []
        t_stack = []
        
        for c in s:
            if c == "#":
                if s_stack:
                    s_stack.pop()
            else:
                s_stack.append(c)
                
        for c in t:
            if c == "#":
                if t_stack:
                    t_stack.pop()
            else:
                t_stack.append(c)
        
        return s_stack == t_stack

print(f"{backspaceCompare(caseS_1, caseT_1)}")
print(f"{backspaceCompare(caseS_2, caseT_2)}")
print(f"{backspaceCompare(caseS_3, caseT_3)}")
print(f"{backspaceCompare(caseS_4, caseT_4)}")