#Maximum Nesting Depth Of The Parentheses
#https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/description/

caseS_1 = "(1+(2*3)+((8)/4))+1"
caseS_2 = "(1)+((2))+(((3)))"

if False:
    def maxDepth(s):
        res_high = 0
        curr_high = 0

        for c in s:
            if c == "(":
                curr_high += 1
                res_high = max(res_high, curr_high)
            elif c == ")":
                curr_high -= 1
            
        return res_high

if True:
    def maxDepth(s):
        arr = []
        d = 0

        for c in s:
            if c == "(":
                arr.append(c)
            elif c == ")":
                d = max(d, len(arr))
                arr.pop()

        return d

print(f"{maxDepth(caseS_1)}")
print(f"{maxDepth(caseS_2)}")