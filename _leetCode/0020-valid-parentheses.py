#Valid Parentheses
#https://leetcode.com/problems/valid-parentheses/description/

caseS_1 = "()"
caseS_2 = "()[]{}"
caseS_3 = "(]"
caseS_4 = "{[]}"
caseS_5 = "([)]"
caseS_6 = "]"
caseS_7 = "(])"

if True:
    def isValid(s):
        
        my_closed_dict = {}
        my_closed_dict["}"] = "{"
        my_closed_dict[")"] = "("
        my_closed_dict["]"] = "["

        my_open_set = set()
        my_open_set.add("{")
        my_open_set.add("(")
        my_open_set.add("[")

        res = ""
        for c in s:
            
            if c in my_open_set:
                res += c
            elif len(res) >= 1 and res[len(res)-1] == my_closed_dict.get(c):
                res = res[:-1]
            elif c in my_closed_dict:
                return False

        return res == ""

if False:
    def isValid(s):
        my_closed_dict = {
            "}":"{",
            "]":"[",
            ")":"("
        }

        my_open_set = set(["{","(","["])

        res = ""
        for c in s:
            
            if c in my_open_set:
                res += c
            elif len(res) >= 1 and res[-1] == my_closed_dict.get(c):
                res = res[:-1]
            elif c in my_closed_dict:
                return False

        return res == ""

if True:
    def isValid(s):
        my_closed_dict = {
            "}":"{",
            "]":"[",
            ")":"("
        }

        my_open_set = set(["{","(","["])

        res = []
        for c in s:
            
            if c in my_open_set:
                res.append(c)
            elif len(res) >= 1 and res[-1] == my_closed_dict.get(c):
                res.pop()
            elif c in my_closed_dict:
                return False

        return len(res) == 0

print(f"{isValid(caseS_1)}")
print(f"{isValid(caseS_2)}")
print(f"{isValid(caseS_3)}")
print(f"{isValid(caseS_4)}")
print(f"{isValid(caseS_5)}")
print(f"{isValid(caseS_6)}")
print(f"{isValid(caseS_7)}")