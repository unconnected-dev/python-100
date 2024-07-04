#Consecutive Characters
#https://leetcode.com/problems/consecutive-characters/description/

caseS_1 = "leetcode"
caseS_2 = "abbcccddddeeeeedcba"

if False:
    def maxPower(s: str) -> int:
        res = 0
        curr_letter = ""
        curr_val = 0

        for c in s:

            if c != curr_letter:
                curr_letter = c
                curr_val = 1
            else:
                curr_val += 1

            res = max(curr_val, res)

        return res
    
if True:
    def maxPower(s: str) -> int:
        res, curr_val = 0, 0

        if(len(s)) == 1:
            return 1

        for i in range(1, len(s)):

            if s[i] != s[i-1]:
                curr_val = 1
            else:
                curr_val += 1
                res = max(res, curr_val)

            res = max(res, curr_val)

        return res

print(f"{maxPower(caseS_1)}")
print(f"{maxPower(caseS_2)}")