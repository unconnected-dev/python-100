#Consecutive Characters
#https://leetcode.com/problems/consecutive-characters/description/

caseS_1 = "leetcode"
caseS_2 = "abbcccddddeeeeedcba"

if True:
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
    
print(f"{maxPower(caseS_1)}")
print(f"{maxPower(caseS_2)}")